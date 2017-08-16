"""Een lijst woorden uit een URL ophalen en afdrukken.


Gebruik: 
    python words.py
"""


from urllib.request import urlopen
import sys

def fetch_words(url):
    """Een lijst woorden uit een URL ophalen.
    
    
    Args:
        url: De URL van een UTF-8 tekstdocument.
        
        
    Retourneert:
        Een lijst strings met woorden uit het document.
    """
    
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return(story_words)


def print_items(items):
    """Drukt één item per regel af. 


    Args:
        items: Een iterable reeks afdrukbare items. 
    """

    for item in items:
        print(item)


def main(url):
    """Drukt elk woord uit een document af dat van een URL komt.


    Args:
        url: De URL van een UTF-8 tekstdocument. 
    """

    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # 0 is de modulebestandsnaam.


