from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.django import Engine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from django.template.loader import get_template
from django.template.base import Template


class MyBackend(BaseEngine):
    app_dirname = 'app'

    def __init__(self, params):
        # Copy the params dictionary to avoid modifying the original
        params = params.copy()

        # Copy the 'OPTIONS' dictionary from params and assign it to the 'options' variable
        options = params.pop('OPTIONS').copy()

        # Call the __init__ method of the parent class
        super().__init__(params)

        # Create an instance of the Engine class with the 'options' dictionary
        self.engine = Engine(**options)

    def get_template(self, template_name: str) -> Template:
        """
        Retrieves a template given its name.

        Args:
            template_name: A string representing the name of the template.

        Returns:
            An instance of the Template class representing the requested template.

        Raises:
            TemplateDoesNotExist: If the template does not exist.
            RecursionError: If there is a recursion error while retrieving the template.

        """
        try:
            # Call the get_template function to retrieve the template
            return Template(get_template(template_name))
        except (TemplateDoesNotExist, RecursionError) as exc:
            # If the template does not exist, raise a TemplateDoesNotExist exception
            # If needed template not found, raise a RecursionError exception
            raise TemplateDoesNotExist(exc.args, backend=self)


class Template:

    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None) -> str:
        """
        Renders the template with the given context and request.

        Args:
            context: A dictionary containing the context variables.
            request: An optional request object.

        Returns:
            A string representing the rendered template.

        """
        # If no context is passed, create an empty dictionary
        if context is None:
            context = {}

        # If a request is passed, add it to the context
        if request is not None:
            context['request'] = request
            context['my_template'] = 'this is custom'

        print(context)

        # Return the result of rendering the template with the context
        return self.template.render(context)
