from flask_restx import Namespace, Resource, fields
from ..models.orders import Order
from http import HTTPStatus
from flask_jwt_extended import jwt_required,get_jwt_identity
from..models.user import User
order_namespace = Namespace('order', description="Namespace for orders")

order_model=order_namespace.model(
    'Order', {
        'id': fields.Integer(description="ID"),
        'size': fields.String(description="size of order", required=True,
                              enum=['SMALL', 'MEDIUM', 'LARGE', 'EXTRA_LARGE']),
        'order_status': fields.String(description="the status of the order",
                                      required=True, enum=['PENDING', 'IN_TRANSIT', 'DELIVERED'])
    }
)


@order_namespace.route('/orders/')
class OrderGetCreate(Resource):
    @order_namespace.marshal_with(order_model)
    @jwt_required()
    def get(self):
        """
            Get all orders

        """
        orders = Order.query.all()

        return orders, HTTPStatus.OK

    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)
    @jwt_required()
    def post(self):
        """
        place a new order

        """

        username=get_jwt_identity()

        current_user=User.query.filter_by(username=username).first()
        data=order_namespace.payload

        new_order=Order(
            siz=data['size'],
            quantity=data['quantity'],
            flavour=data['flavour']

        )

        new_order.user=current_user
        new_order.save()

        return new_order, HTTPStatus.CREATED


@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):
    def get(self, order_id):
        """
            Retrieve an order
        :param order_id:
        :return:
        """
        pass

    def put(self, order_id):
        """
            Update an order with id
        :param order_id:
        :return:
        """
        pass

    def delete(self, order_id):
        """
            Delete an order
        :param order_id:
        :return:
        """
        pass


@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):
    def get(self, user_id, order_id):
        """
            Get Users Specific Order
        :param user_id:
        :param order_id:
        :return:
        """
        pass


@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):
    def get(self, user_id):
        """
        Get all orders by a specific user
        :param user_id:
        :return:
        """

        pass


@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):
    def patch(self, order_id):
        """
            Update an order status
        :param order_id:
        :return:
        """
        pass
