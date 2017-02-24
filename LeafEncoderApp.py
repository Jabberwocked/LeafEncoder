from flask import Flask, jsonify
from flask import request

from LeafNameEncoder.Leaf import Leaf
from LeafNameEncoder.ValueTypes.ValueTypeMap import ValueType

app = Flask(__name__)

@app.route("/<string:encodedLeaf>/", methods=['GET'])
def index(encodedLeaf):
    sut = Leaf()
    values = [(ValueType.DayHour, (5, 17)), (ValueType.UInt, 2294967295)]
    # act
    decoded = sut.decode(encodedLeaf)
    return {}
    #sut.create(values)

if __name__ == '__main__':
    app.run()