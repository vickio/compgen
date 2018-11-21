from pathlib import Path

from card_page import CardPage

outfile = Path('html/index.html')
outfile.write_text(CardPage(100).html, 'utf8')

