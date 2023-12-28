from flask import jsonify

def populate_object(obj, data_dict):
    fields = data_dict.keys()

    for field in fields:
        try: 
            getattr(obj, field)
            setattr(obj, field, data_dict[field])
        
        except:
            return jsonify({"error message": f"record has no attribute {field}"})
