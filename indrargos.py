import requests
from bs4 import BeautifulSoup

class Indrargos:
    def see(url):
        """
        Extract headlines and content from a given URL.
        
        Gets h1,h2 tags and elements with largest font size using CSS.
        """
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all h1 and h2 tags
            h1_tags = soup.find_all('h1')
            h2_tags = soup.find_all('h2')
            
            # Find elements with largest font size using CSS
            largest_font_elements = soup.select('[style*="font-size"]')
            
            # Extract the headlines from h1, h2 tags, and largest font elements
            headlines = [tag.text for tag in h1_tags] + [tag.text for tag in h2_tags]
            headlines += [element.text for element in largest_font_elements]
            
            # Remove any duplicate headlines
            headlines = list(set(headlines))
            
            # Extract the content associated with each headline
            content = {headline: "..." for headline in headlines}
            
            return {'headlines': headlines, 'content': content}
        
        # Return an empty result if the request was not successful
        return {'headlines': [], 'content': {}}
    
    def investigate(url):
        """
        Given a url, gets article text and images.
        """
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all paragraphs in the article
            paragraphs = soup.find_all('p')
            
            # Extract the text from each paragraph
            text = [p.text for p in paragraphs]
            
            # Find all images in the article
            images = soup.find_all('img')
            
            # Extract the URLs of the images
            image_urls = [img['src'] for img in images]
            
            return {'text': text, 'images': image_urls}
        
        # Return an empty result if the request was not successful
        return {'text': [], 'images': []}
        