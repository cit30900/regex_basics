import re

def main():
    filestring = "pretty.bmp, successful.json, international.mp3, office.docx, send.wav, small.webm, design.csv, smile.docx, food.wav, view.pdf, pull.js, cover.mp3, leader.numbers, value.flac, yourself.webm, four.mp3, if.wav, break.jpeg, example.xlsx, my.jpeg.json, former.mp4, at.txt, religious.css, mind.avi, babybmp.bmp, note.mp3, begin.flac, push.flac, later.gif, live.css, life.json, cover.flac, think.mp4, company.json, poor.png, present.odt, five.css, v.gif, happen.mp4, CASE.gif, T.gif, case.bmp, interesting.json, that.odt, rather.jpg, old.webm, generation.html, compare.mov, station.mp4, hand.js"

    imagefiles = re.findall(r"\b[a-zA-Z]+\.(?:jpeg|jpg|bmp|gif|png)", filestring)
    print(imagefiles)

    # Progression to our more complex regular expression:
        # jpeg
        # \.jpeg
        # \.(jpeg|jpg)
        # \.(jpeg|jpg|bmp|gif|png)
        # \.(?:jpeg|jpg|bmp|gif|png)
        # [a-z]\.(?:jpeg|jpg|bmp|gif|png)
        # \b[a-z]\.(?:jpeg|jpg|bmp|gif|png)
        # \b[a-z]+\.(?:jpeg|jpg|bmp|gif|png)
        # \b[a-zA-Z]+\.(?:jpeg|jpg|bmp|gif|png)

if __name__== "__main__":
  main()