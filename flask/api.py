### Put and Delete-HTTP Verbs
### Working With API's--Json

from flask import Flask,jsonify,request

app = Flask(__name__)

##Initial Data in my to do list
items = [
    {'id':1,'name':'item 1','description':'this is item 1'},
    {'id':2,'name':'item 2','description':'this is item 2'}
]

@app.route('/')
def home():
    return "Welcome To Home Page"

##Get : retrive all the items
@app.route('/item',methods= ['GET'])
def get_items():
    return jsonify(items)

##Get : retrive a specific item by id
@app.route('/item/<int:id>',methods=['GET'])
def get_item(id):
    item=next((item for item in items if item ['id']==id),None)
    if item is None:
        return jsonify({'error':"Item Not Found"})
    return jsonify(item)

##Post : Create a new Item - API
@app.route('/item',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'Item Not Found'})
    new_item={
        'id':items[-1]['id']+1 if items else 1,
        'name':request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

##Put : Update existing item
@app.route('/item/<int:id>',methods=['PUT'])
def update_item(id):
    item=next((item for item in items if item["id"]==id),None)
    if item is None:
        return jsonify({'error':'Item Not Found'})
    item['name']=request.json.get('name',item['name']),
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

#Delete : Delete an item
@app.route('/item/<int:id>',methods=['DELETE'])
def delete_item(id):
    global items
    items = [item for item in items if item['id']!=id]
    return jsonify({'result':'Item Deleted'})
    

if __name__=='__main__':
    app.run(debug = True)