from model import Model
from view import View


class Controller:
    def __init__(self, view: View, model: Model):
        """_summary_

        Args:
            view (View): view is for bounding bet gui object and event handler
            model (Model): _description_
        """
        self.view = view
        self.model = model

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)
