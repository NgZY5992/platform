from flask import Blueprint, request
from app.models.image import Image
from app import db
from util.response_codes import ResponseBuilder, ResponseCode

image_blueprint = Blueprint('image', __name__)

@image_blueprint.route('/list', methods=['GET'])
def get_images():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 10))

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    images = Image.query.slice(start_idx, end_idx).all()

    result_images = [{'id': image.id, 'name': image.name, 'url': image.url} for image in images]

    return ResponseBuilder.build_response(ResponseCode.OK, data=result_images)

@image_blueprint.route('/get/<int:image_id>', methods=['GET'])
def get_image(image_id):
    image = Image.query.get(image_id)

    if image is None:
        return ResponseBuilder.build_response(ResponseCode.NOT_FOUND, message='Image not found')

    result_image = {'id': image.id, 'name': image.name, 'url': image.url}
    
    return ResponseBuilder.build_response(ResponseCode.OK, data=result_image)

@image_blueprint.route('/create', methods=['POST'])
def create_image():
    data = request.json

    if not data or 'name' not in data or 'url' not in data:
        return ResponseBuilder.build_response(ResponseCode.BAD_REQUEST, message='Invalid data')

    new_image = Image(name=data['name'], url=data['url'])
    db.session.add(new_image)
    db.session.commit()

    return ResponseBuilder.build_response(ResponseCode.CREATED, data={'id': new_image.id})

@image_blueprint.route('/update/<int:image_id>', methods=['PUT'])
def update_image(image_id):
    image = Image.query.get(image_id)

    if image is None:
        return ResponseBuilder.build_response(ResponseCode.NOT_FOUND, message='Image not found')

    data = request.json

    if not data or 'name' not in data or 'url' not in data:
        return ResponseBuilder.build_response(ResponseCode.BAD_REQUEST, message='Invalid data')

    image.name = data['name']
    image.url = data['url']
    db.session.commit()

    return ResponseBuilder.build_response(ResponseCode.OK, message='Image updated successfully')

@image_blueprint.route('/delete/<int:image_id>', methods=['DELETE'])
def delete_image(image_id):
    image = Image.query.get(image_id)

    if image is None:
        return ResponseBuilder.build_response(ResponseCode.NOT_FOUND, message='Image not found')

    db.session.delete(image)
    db.session.commit()

    return ResponseBuilder.build_response(ResponseCode.OK, message='Image deleted successfully')
