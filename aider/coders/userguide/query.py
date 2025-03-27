import openai
import os
import pandas as pd
import ast
from scipy import spatial
import tiktoken
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to get API key from environment
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client only if API key is available
client = None
if api_key:
    try:
        client = openai.OpenAI(api_key=api_key)
    except Exception as e:
        logger.error(f"Failed to initialize OpenAI client: {e}")

# Load embeddings from CSV
try:
    df = pd.read_csv("aider/aider/coders/userguide/userguide_embeddings.csv")
    df['embedding'] = df['embedding'].apply(ast.literal_eval)
except Exception as e:
    logger.error(f"Failed to load embeddings: {e}")
    # Create an empty DataFrame with required columns as fallback
    df = pd.DataFrame(columns=["text", "embedding"])

EMBEDDING_MODEL = "text-embedding-3-small"
GPT_MODEL = "gpt-4o"

def strings_ranked_by_relatedness(
        query: str,
        df: pd.DataFrame,
        relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
        top_n: int = 100
) -> tuple[list[str], list[float]]:
    """Returns a list of strings and relatedness, sorted from most related to least related."""
    
    # Check if client is available
    if not client:
        logger.warning("OpenAI client not initialized, returning empty results")
        return [], []
    
    # Check if DataFrame is empty
    if df.empty:
        logger.warning("DataFrame is empty, returning empty results")
        return [], []
    
    try:
        # Fix the API call to match the new OpenAI client syntax
        query_embedding_response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=query  # Changed from 'inputs' to 'input'
        )
        query_embedding = query_embedding_response.data[0].embedding
        
        strings_and_relatedness = [
            (row["text"], relatedness_fn(query_embedding, row["embedding"]))
            for i, row in df.iterrows()
        ]

        strings_and_relatedness.sort(key=lambda x: x[1], reverse=True)
        strings, relatedness = zip(*strings_and_relatedness)
        return strings[:top_n], relatedness[:top_n]
    except Exception as e:
        logger.error(f"Error in relatedness calculation: {e}")
        return [], []
    
def num_tokens(text: str, model: str = GPT_MODEL) -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except Exception:
        # Fallback token estimation
        return len(text) // 4

def query_message(
        query: str,
        df: pd.DataFrame = df, 
        model: str = GPT_MODEL, 
        token_budget: int = 4096-500
) -> str:
    """Return a message for GPT that, with relevant source texts pulled from a dataframe."""
    try:
        strings, relatedness = strings_ranked_by_relatedness(query, df)
        
        if not strings:
            return "Unable to retrieve relevant sections from the user guide."
            
        message = ""
        for string in strings:
            next_article = f'\n\nUser Guide section:\n"""\n{string}\n"""'
            if (
                num_tokens(message + next_article, model) > token_budget
            ):
                break
            else:
                message += next_article
        return message
    except Exception as e:
        logger.error(f"Error in query_message: {e}")
        return "An error occurred while searching the user guide. Proceeding without user guide references."