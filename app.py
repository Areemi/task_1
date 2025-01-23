from flask import Flask, request, jsonify, render_template, redirect, url_for
from orm import Vehicle, Car, Motorcycle, Session
from forms import VehicleForm

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'your_secret_key'  # Измените на ваш секретный ключ

session = Session()

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = session.query(Vehicle).all()
    return jsonify({'vehicles': [veh.as_dict() for veh in vehicles]})

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.get_json()
    if data['type'] == 'car':
        vehicle = Car(brand=data['brand'], model=data['model'], num_doors=data['num_doors'])
    else:
        vehicle = Motorcycle(brand=data['brand'], model=data['model'], has_sidecar=data['has_sidecar'])
    session.add(vehicle)
    session.commit()
    return jsonify({'message': 'Vehicle added successfully', 'vehicle': vehicle.as_dict()})

@app.route('/vehicles/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    vehicle = session.query(Vehicle).get(vehicle_id)
    if not vehicle:
        return jsonify({'message': 'Vehicle not found'}), 404
    data = request.get_json()
    vehicle.brand = data['brand']
    vehicle.model = data['model']
    if isinstance(vehicle, Car):
        vehicle.num_doors = data['num_doors']
    elif isinstance(vehicle, Motorcycle):
        vehicle.has_sidecar = data['has_sidecar']
    
    session.commit()
    return jsonify({'message': 'Vehicle updated successfully', 'vehicle': vehicle.as_dict()})

@app.route('/vehicles/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    vehicle = session.query(Vehicle).get(vehicle_id)
    if not vehicle:
        return jsonify({'message': 'Vehicle not found'}), 404
    session.delete(vehicle)
    session.commit()
    return jsonify({'message': 'Vehicle deleted successfully'})

@app.route('/add_vehicle', methods=['GET', 'POST'])
def add_vehicle_form():
    form = VehicleForm()
    if form.validate_on_submit():
        if form.type.data == 'car':
            vehicle = Car(brand=form.brand.data, model=form.model.data, num_doors=form.num_doors.data)
        else:
            vehicle = Motorcycle(brand=form.brand.data, model=form.model.data, has_sidecar=form.has_sidecar.data)
        session.add(vehicle)
        session.commit()
        return redirect(url_for('get_vehicles'))
    return render_template('add_vehicle.html', form=form)

@app.route('/edit_vehicle/<int:vehicle_id>', methods=['GET', 'POST'])
def edit_vehicle(vehicle_id):
    vehicle = session.query(Vehicle).get_or_404(vehicle_id)
    form = VehicleForm(obj=vehicle)
    
    if form.validate_on_submit():
        vehicle.brand = form.brand.data
        vehicle.model = form.model.data
        
        if isinstance(vehicle, Car):
            vehicle.num_doors = form.num_doors.data
        elif isinstance(vehicle, Motorcycle):
            vehicle.has_sidecar = form.has_sidecar.data
        
        session.commit()
        return redirect(url_for('get_vehicles'))

    return render_template('edit_vehicle.html', form=form, vehicle=vehicle)

if __name__ == '__main__':
    app.run(debug=True)