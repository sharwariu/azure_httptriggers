
import azure.functions as func
import logging

app = func.FunctionApp()

books=['rich dad poor dad','Lord of the Rings','Pinocchio']
@app.function_name(name="view_books")
@app.route(route="view_books",methods=[func.HttpMethod.GET])
def view_books(req:func.HttpRequest) -> func.HttpResponse:
    logging.info(books)
    return str(books)

@app.route(route="add_book",methods=[func.HttpMethod.PUT])
def add_book(req:func.HttpRequest)->func.HttpResponse:
     name = req.params.get('name')
     if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

     if name:
        books.append(name)
        return f'Successfully added order: {books}'
     else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query to add book.",
             status_code=200
        )

      

@app.route(route="delete_book",methods=[func.HttpMethod.DELETE])
def delete_book(req:func.HttpRequest)->func.HttpResponse:
    logging.info(books)
    books.pop()
    return f'Successfully deleted order: {books}'