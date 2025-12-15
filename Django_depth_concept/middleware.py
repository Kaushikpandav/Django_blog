



# Middleware:

    from traceback import print_tb
Middleware : it's piece of code which run between request and response. used to secure the system or add some features to the system.

    - in build-in middleware : SecurityMiddleware, SessionMiddleware, AuthenticationMiddleware, MessageMiddleware, ,AuthenticationMiddleware
    - Custom middleware :  You can create your own middleware to add some features to the system.
                        # Custom middleware:
                        - create a file in app : middleware.py
                        - create a class in middleware.py
                        - add this class in settings.py > MIDDLEWARE

===================================================

NOTE:  middleware will run for all the views. not any specific view.




#Custom middleware:
1) function based middleware : 


    def my_fun_middleware(get_response):
        print("Middleware : One time Initialization... ")
        def middleware(request):
            print("write logic here, which you want to execute before view respond")
            res = get_response(request)
            print("It's after views ")
            return res
        return middleware

    # for custom response without call view from get_response() WE CAN CALL templates or Httpsresponse
    # def my_fun_middleware(get_response):
    #     print("Middleware : One time Initialization... ")
    #     def middleware(request):
    #         print("write logic here, which you want to execute before view respond")
    #         res = HttpResponse("Coming Soon...")
    #         print("It's after views ")
    #         return res
    #     return middleware

    # to activate the middleware : add fucntion name in settings.py > MIDDLEWARE


2) Class based middleware : 

    class myclassmiddle:
        def __init__(self, get_response):
            self.get_response = get_response
            print(f"One time initializations... ")

        def __call__(self, request):
            print(f"Before calling view code")
            res = self.get_response(request)
            print(f"After calling view code")
            return res

    # to activate the middleware : add class name in settings.py > MIDDLEWARE



3) what if multi inheritance middleware calls : 



class myclassmiddle1:
        def __init__(self, get_response):
            self.get_response = get_response
            print(f"One time initializations... ")

        def __call__(self, request):
            print(f"Before calling view code")
            res = self.get_response(request)
            print(f"After calling view code")
            return res
        
class myclassmiddle2:
        def __init__(self, get_response):
            self.get_response = get_response
            print(f"One time initializations... ")

        def __call__(self, request):
            print(f"Before calling view code")
            res = self.get_response(request)
            print(f"After calling view code")
            return res

class myclassmiddle3:
        def __init__(self, get_response):
            self.get_response = get_response
            print(f"One time initializations... ")

        def __call__(self, request):
            print(f"Before calling view code")
            res = self.get_response(request)
            print(f"After calling view code")
            return res

# to activate the middleware : add class name in settings.py > MIDDLEWARE (make sure each middleware is unique and in order based on priority)


4) Hooks in middleware : 

class myclassmiddle4:
        def __init__(self, get_response):
            self.get_response = get_response
            print(f"One time initializations... ")

        def __call__(self, request):
            print(f"Before calling view code")
            res = self.get_response(request)
            print(f"After calling view code")
            return res

        #used to run logic before view calss.
        def process_view(self, request, view_func, view_args, view_kwargs):
            print(f"Before calling view function")
            # return HttpResponse("Coming Soon...") we can rander a template as well.
            return view_func(request, *view_args, **view_kwargs)
            # return None : if i return None then it will not call the view function.

        #used to run logic after view calss.
        def process_response(self, request, response):
            print(f"After calling view function")
            return response

        #used to handle the exception .
        def process_exception(self, request, exception):
            exception_msg = exception
            class_name  = exception.__class__.__name__
            print(f"Exception")
            print(class_name)
            print(exception_msg)
            return HttpResponse(exception_msg + " " + class_name)

        # used to run logic after template response. and manipulate the response at run time. 
        def process_template_response(self, request, response):
            print(f"Template response")
            response.context_data['name'] = 'Kaushik'
            return response

5) async middleware : 







================================

    # EX: Views.py
    def home(request):
        print("Views : Home")
        return render(request, 'home.html')

 