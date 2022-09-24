
from flask import Flask, request

app=Flask(__name__)

org =['Oracle', 'Google', 'Microsoft', 'Amazon', 'Deloitte']

@app.route('/',methods=['GET'])
def intro():
    return "!!Text Replace Program!!"

@app.route('/replace_txt/<srch_str>', methods=['POST'])
def replace_txt(srch_str):
    #srch_str = request.args.get('srch_string')
    str_list = srch_str.split()
    try:
        for loc,item in enumerate(str_list):
            if item in org:
                rplcd_word = str_list[loc]
                rplcd_word = rplcd_word+"\u00a9"
                str_list.pop(loc)
                str_list.insert(loc, rplcd_word)
            # else:
            #      final_str = '!!No Keyword Found to be replaced!!'
        final_str = ' '.join(str_list)
    except:
        final_str = 'Error'
    
    return final_str

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=80)