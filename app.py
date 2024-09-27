from flask import Flask, request, jsonify
from collections import deque
from datetime import datetime

app = Flask(__name__)

transactions = deque()
payer_balances = {}

@app.route('/add', methods=['POST'])
def add_points():
    data = request.get_json()
    payer = data['payer']
    points = data['points']
    timestamp = data['timestamp']
    
    # Parse timestamp
    transaction = {
        'payer': payer,
        'points': points,
        'timestamp': datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    }
    transactions.append(transaction)

    # Update points
    if payer in payer_balances:
        payer_balances[payer] += points
    else:
        payer_balances[payer] = points

    return '', 200

@app.route('/spend', methods=['POST'])
def spend_points():
    points_to_spend = request.get_json()['points']
    if points_to_spend > sum(payer_balances.values()):
        return 'Not enough points', 400
    
    # Sort transactions
    spent_points = []
    remaining_points = points_to_spend
    
    while remaining_points > 0 and transactions:
        transaction = transactions.popleft()
        payer = transaction['payer']
        points = transaction['points']
        
        if points <= remaining_points:
            remaining_points -= points
            payer_balances[payer] -= points
            spent_points.append({'payer': payer, 'points': -points})
        else:
            transactions.appendleft({
                'payer': payer,
                'points': points - remaining_points,
                'timestamp': transaction['timestamp']
            })
            payer_balances[payer] -= remaining_points
            spent_points.append({'payer': payer, 'points': -remaining_points})
            remaining_points = 0

    return jsonify(spent_points), 200

@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(payer_balances), 200


if __name__ == '__main__':
    app.run(port=8000)
