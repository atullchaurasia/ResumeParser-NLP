import re
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_section(text, section_headers, stop_headers):
    start_pattern = re.compile('|'.join(re.escape(header) for header in section_headers), re.IGNORECASE)
    stop_pattern = re.compile('|'.join(re.escape(header) for header in stop_headers), re.IGNORECASE)

    start_match = start_pattern.search(text)
    if not start_match:
        return ""

    start_pos = start_match.end()
    stop_match = stop_pattern.search(text, start_pos)
    if stop_match:
        end_pos = stop_match.start()
        return text[start_pos:end_pos].strip()
    return text[start_pos:].strip()

def clean_text(text):
    cleaned_text = text.replace('\n', ' ')
    return cleaned_text

def extract_mobile_number(text):
    phone_pattern = re.compile(
        r"\b(\+?\d{1,4}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?(\d{3}[-.\s]?\d{4})\b"
    )
    matches = phone_pattern.findall(text)
    if matches:
        # Flatten the list of tuples into a single string
        return ''.join([''.join(match) for match in matches[0] if match])
    else:
        return None

def extract_email_id(text):
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    matches = email_pattern.findall(text)
    if matches:
        return matches[0]
    else:
        return None

def extract_candidate_name(text):
    # Assuming the candidate's name is the first line in the text
    lines = text.split("\n")
    for line in lines:
        if line.strip():  # Return the first non-empty line
            return line.strip()
    return None 


def extract_links_extended(text):
    """
    Extracts and returns a list of links from the given text.

    Args:
        text (str): The text to extract links from.

    Returns:
        list: A list of strings representing the links extracted from the text.
    """
    links = []
    try:
        pattern = r'(http[s]?://\S+|ftp://\S+|mailto:\S+|linkedin.com/\S+|github.com/\S+|twitter.com/\S+)'
        raw_links = re.findall(pattern, text)
        for link in raw_links:
            links.append(link)
    except Exception as e:
        print(f"Error extracting links: {str(e)}")
    return links

def find_unmatched_text(full_text, *sections):
    combined_sections_text = " ".join(sections)
    combined_sections_text = re.sub(r'\s+', ' ', combined_sections_text).strip()
    full_text_words = set(re.sub(r'\s+', ' ', full_text).strip().split())
    combined_sections_words = set(combined_sections_text.split())
    unmatched_words = full_text_words - combined_sections_words
    return " ".join(unmatched_words)

def pos_words_tokenize(text):
    words = word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    return pos_tags

    
def word_frequency_distribution(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    freq_dist = FreqDist(filtered_words)
    return freq_dist.most_common(30)

