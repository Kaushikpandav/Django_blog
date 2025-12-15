# Abstract Overviews topics :



===================================================

1.  signals :

    i) Build-in: 1) LOGIN/OUT: - user_logged_in, user_logged_out, user_login_failed()

        from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
        from django.contrib.auth.models import User
        from django.dispatch import receiver

        def user_logged_in(sender, request, user, \*\*kwargs):
            print(f"User {user} logged in.")
        user_logged_in.connect(user_logged_in, sender=User)
        # or with decorator
        @receiver(user_logged_in, sender=User)
        def user_logged_in(sender, request, user, \*\*kwargs):
            print(f"User {user} logged in.")


        def user_logged_out(sender, request, user, **kwargs):
            print(f"User {user} logged out.")
        user_logged_out.connect(user_logged_out, sender=User)
        # or with decorator
        @receiver(user_logged_out, sender=User)
        def user_logged_out(sender, request, user, **kwargs):
            print(f"User {user} logged out.")

        def user_login_failed(sender, credentials, **kwargs):
            print(f"User {credentials['username']} login failed.")
        user_login_failed.connect(user_login_failed)
        # or with decorator
        @receiver(user_login_failed)
        def user_login_failed(sender, credentials, request, **kwargs):
            print(f"User {credentials['username']} login failed.")


        NOTE : add config in apps.py
        from django.apps import AppConfig
        class BlogConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'blog'

            def ready(self):
                import blog.signals


    2) More signals:
    
    # from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, pre_init, post_init, m2m_changed, pre_migrate, post_migrate
    # from django.dispatch import receiver
    # from django.core.signals import request_started, request_finished, got_request_exception
    # from django.db.backends.signals import connection_created, connection_closed

    # @receiver(pre_save, sender=User)
    # def my_pre_save(sender, instance, **kwargs):
    #     print("Pre-save signal triggered")
    
    # @receiver(post_save, sender=User)
    # def my_post_save(sender, instance, created, **kwargs):
    #     if created:
    #         print("Post-save signal triggered")
    #         print(f"New user created: {instance}")
    #     else:
    #         print("Post-save signal triggered")
    #         print(f"User updated: {instance}")
    
    # @receiver(pre_delete, sender=User)
    # def my_pre_delete(sender, instance, **kwargs):
    #     print("Pre-delete signal triggered")
    #     print(f"User: {sender}")
    #     print(f"User deleted: {instance}")
    
    # @receiver(post_delete)
    # def my_post_delete(sender, instance, **kwargs):
    #     print("Post-delete signal triggered")
    #     print(f"User: {sender}")
    #     print(f"User deleted: {instance}")
    
    # at time of initialization
    # @receiver(pre_init, sender=User)
    # def my_pre_init(sender, **kwargs):
    #     print("Pre-init signal triggered")
    #     print(f"User: {sender}")
    
    # @receiver(post_init, sender=User)
    # def my_post_init(sender, **kwargs):
    #     print("Post-init signal triggered")
    #     print(f"User: {sender}")
    
    # @receiver(pre_migrate)
    # def my_pre_migrate(sender, app_config, verbosity, interactive, plan, connection, using, **kwargs):
    #     print("Pre-migrate signal triggered")
    #     print(f"App config: {app_config}")
    #     print(f"Verbosity: {verbosity}")
    #     print(f"Interactive: {interactive}")
    #     print(f"Plan: {plan}")
    #     print(f"Connection: {connection}")
    #     print(f"Using: {using}")
    
    # @receiver(post_migrate)
    # def my_post_migrate(sender, app_config, verbosity, interactive, plan, connection, using, **kwargs):
    #     print("Post-migrate signal triggered")
    #     print(f"App config: {app_config}")
    #     print(f"Verbosity: {verbosity}")
    #     print(f"Interactive: {interactive}")
    #     print(f"Plan: {plan}")
    #     print(f"Connection: {connection}")
    #     print(f"Using: {using}")


    # at time of HTTPrequest
    # @receiver(request_started)
    # def my_request_started(sender, request,environ, **kwargs):
    #     print("Request started signal triggered")
    #     print(f"Request: {request}")
    #     print(f"Environ: {environ}")

    # @receiver(request_finished)
    # def my_request_finished(sender, request, **kwargs):
    #     print("Request finished signal triggered")
    #     print(f"Request: {request}")

    # @receiver(got_request_exception)
    # def my_got_request_exception(sender, request, **kwargs):
    #     print("Got request exception signal triggered")
    #     print(f"Request: {request}")

    # at time of database CREATION
    # @receiver(connection_created)
    # def my_connection_created(sender, connection, **kwargs):
    #     print("Connection created signal triggered")
    #     print(f"Connection: {connection}")

    # @receiver(connection_closed)
    # def my_connection_closed(sender, connection, **kwargs):
    #     print("Connection closed signal triggered")
    #     print(f"Connection: {connection}")

    # @receiver(m2m_changed, sender=User)
    # def my_m2m_changed(sender, instance, **kwargs):
    #     print("M2M changed signal triggered")


2) Custom signals : 
    
    # - In signals.py
    from django.dispatch import Signal
    notification_signal = Signal()

    # RECIEVER FUNCTION
    @receiver(notification_signal)
    def notification_signal_receiver(sender, **kwargs):
        print("Notification signal received")
        print(f"Sender: {sender}")
        print(f"Keyword arguments: {kwargs}")


    # - In views.py import signals and send signal
    # EX:
    from your_app_name.signals import notification_signal

    def Home(request):
        notification_signal.send(sender=request.user, message="Hello, world!", User=request.user)