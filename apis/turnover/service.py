from bson.objectid import ObjectId

from database import get_collection

turnover_collection = get_collection('turnover')


# Serialize the database result to a dictionary
def turnover_serializer(turnover) -> dict:
    return {
        'id': str(turnover['_id']),
        'date': turnover['date'],
        'tiCai': turnover['ti_cai'],
        'waiDian': turnover['wai_dian'],
        'fuCai': turnover['fu_cai'],
        'onePercent': turnover['one_percent'],
    }


# Retrieve all turnovers present in the database
def retrieve_turnovers():
    turnovers = []
    for turnover in turnover_collection.find():
        turnovers.append(turnover_serializer(turnover))
    return turnovers


# Add a new turnover into to the database
def add_turnover(turnover_data: dict) -> dict:
    turnover = turnover_collection.insert_one(turnover_data)
    new_turnover = turnover_collection.find_one(
        {'_id': turnover.inserted_id})
    return turnover_serializer(new_turnover)


# Retrieve a turnover with a matching ID
def retrieve_turnover(id: str) -> dict:
    turnover = turnover_collection.find_one({'_id': ObjectId(id)})
    if turnover:
        return turnover_serializer(turnover)


# Retrieve a turnover with a matching date
def retrieve_turnover_by_date(date: str) -> dict:
    turnover = turnover_collection.find_one({'date': date})
    if turnover:
        return turnover_serializer(turnover)


# Update a turnover with a matching ID
def update_turnover(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    turnover = turnover_collection.find_one({'_id': ObjectId(id)})
    if turnover:
        updated_turnover = turnover_collection.update_one(
            {'_id': ObjectId(id)}, {'$set': data})
        if updated_turnover:
            return True
        return False


# Update a turnover with a matching date
def update_turnover_by_date(date: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    turnover = turnover_collection.find_one({'date': date})
    if turnover:
        updated_turnover = turnover_collection.update_one(
            {'date': date}, {'$set': data})
        if updated_turnover:
            return True
        return False


# Delete a turnover from the database
def delete_turnover(id: str):
    turnover = turnover_collection.find_one({'_id': ObjectId(id)})
    if turnover:
        turnover_collection.delete_one({'_id': ObjectId(id)})
        return True
