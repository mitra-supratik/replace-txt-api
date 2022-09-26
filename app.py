'''
Author: Supratik Mitra
Date: September 2022
Description: API to add copyright sympbol to organization names
'''

from flask import Flask, request

app=Flask(__name__)

org =['Oracle', 'Google', 'Microsoft', 'Amazon', 'Deloitte']

@app.route('/',methods=['GET'])
def intro():
    return "!!Welcome to Orgname Check!!"

@app.route('/replace_txt/<srch_str>', methods=['POST'])
def replace_txt(srch_str):
    str_list = srch_str.split()
    try:
        for loc,item in enumerate(str_list):
            if item in org:
                rplcd_word = str_list[loc]
                rplcd_word = rplcd_word+"\u00a9"
                str_list.pop(loc)
                str_list.insert(loc, rplcd_word)
        final_str = ' '.join(str_list)
    except:
        final_str = 'Error'
    
    return final_str

if __name__ == "__main__":
    app.run()