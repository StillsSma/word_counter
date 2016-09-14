with open("sample.txt") as better_open_file:
    better_contents = better_open_file.read()
    exclude = """.,?;!":$#%&*()'"""
    for item in exclude:
            better_contents = better_contents.replace(item, "")
    better_contents = better_contents.lower()
    better_contents = better_contents.replace("\n", " ")
    better_contents = better_contents.split(" ")
    for word in better_contents:
        print (word)
    excluded_words = """a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you," ", your"""
    excluded_words = excluded_words.replace("\n", "")
    excluded_words = excluded_words.split(",")
    for word in excluded_words:
        print (word)
