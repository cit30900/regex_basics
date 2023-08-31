import re

def main():
    filelist = ['music.xls', 'international.ppt', 'arrive.ppt', 'tough.ppt', 'service.ppt', 'along.pdf', 'per.odt', 'without.numbers', 'stop.numbers', 'life.pdf', 'maintain.pdf', 'yard.docx', 'foot.xlsx', 'as.pages', 'TYPE.DOC', 'check.docx', 'bar.odp', 'life.key', 'return.xlsx', 'explain.ppt', 'clearly.ppt', 'nation.pdf', 'concern.numbers', 'continue.numbers', 'pattern.odt', 'executive.pdf', 'culture.numbers', 'wrong.doc', 'generation.docx', 'that.pdf', 'womaN.XLS', 'eight.ppt', 'politics.odp', 'growth.odp', 'far.odt', 'them.key', 'since.ppt', 'least.numbers', 'rest.docx', 'anyone.numbers', 'happen.key', 'my.key', 'a.ods', 'new.odp', 'traditional.pptx', 'responsibility.numbers', 'employee.odp', 'picture.doc', 'keep.xlsx', 'believe.doc']

    # Progression to our more complex regular expression:
        # xls|doc|ppt
        # \.(xls|doc|ppt)
        # \.(?:xls|doc|ppt)
        # \.(?:xls|doc|ppt)\b
        # [a-z]\.(?:xls|doc|ppt)\b
        # [a-z0-9]\.(?:xls|doc|ppt)\b
        # [a-z0-9]+\.(?:xls|doc|ppt)\b

    oldfiles = []

    oldfiles = [f for f in filelist if re.search(r"[a-z0-9]+\.(?:xls|doc|ppt)\b", f, re.IGNORECASE)]

    print(oldfiles)

if __name__== "__main__":
  main()