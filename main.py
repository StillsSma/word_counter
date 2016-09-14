with open("sample.txt") as better_open_file:
    better_contents = better_open_file.read()
    exclude = """.,?;!":$#%&*()'"""
    for item in exclude:
            better_contents = better_contents.replace(item, "")
    better_contents = better_contents.lower()
    better_contents = better_contents.replace("\n", " ")
    better_contents = better_contents.split(" ")
    excluded_words = """a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your"""
    excluded_words = excluded_words.replace("\n", "")
    excluded_words = excluded_words.split(",")
    for words in excluded_words:
        while words in better_contents:
            better_contents.remove(words)

    word_count = {}
    for words in better_contents:
        if words in word_count.keys():
            word_count[words] += 1
        else:
            word_count[words] = 1

    word_count = (sorted(word_count.items(), key=lambda x: x[1]))
    word_count = word_count[-21:-1]
    for words in reversed(word_count):
        print (*words)
