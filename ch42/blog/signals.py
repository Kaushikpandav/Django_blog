from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


# @receiver(user_logged_in)
# def on_user_logged_in(sender, user, request, **kwargs):
#   print(f"User logged in: {user.username}")


# @receiver(user_logged_out)
# def on_user_logged_out(sender, user, request, **kwargs):
#   print(f"User logged out: {user.username}")


# @receiver(user_login_failed)
# def on_user_login_failed(sender, credentials, request, **kwargs):
#   print(f"User login failed: {credentials}")



from django.contrib.auth.signals import pre_init, pre_save, pre_delete, pre_migrate, post_init, post_save, post_delete, post_migrate , request_started, request_finished,got_request_exception, connection_created



@receiver(pre_save, sender=User)
def on_pre_save(sender, instance, **kwargs):
  print(f"User pre_save: {instance.username}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")

@receiver(post_save, sender=User)
def on_post_save(sender, instance, created, **kwargs):
  if created:
    print(f"User created: {instance.username}")
    print(f"User post_save: {instance.username}")
    print(f"sender : {sender}")
    print(f"kwargs : {kwargs}")
  else:
    print(f"User updated: {instance.username}")
    print(f"User post_save: {instance.username}")
    print(f"sender : {sender}")
    print(f"kwargs : {kwargs}")

@receiver(pre_delete, sender=User)
def on_pre_delete(sender, instance, **kwargs):
  print(f"User pre_delete: {instance.username}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")

@receiver(post_delete, sender=User)
def on_post_delete(sender, instance, **kwargs):
  print(f"User post_delete: {instance.username}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")


@receiver(pre_init, sender=User)
def on_pre_init(sender, instance, **kwargs):
  print(f"User pre_init: {instance.username}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")

@receiver(post_init, sender=User)
def on_post_init(sender, instance, **kwargs):
  print(f"User post_init: {instance.username}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")

@receiver(pre_migrate, sender=User)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps,  **kwargs):
  print(f"User pre_migrate: {app_config.name}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")


@receiver(post_migrate, sender=User)
def on_post_migrate(sender, instance, **kwargs):
  print(f"User post_migrate: {instance.username}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")


@receiver(request_started)
def on_request_started(sender, **kwargs):
  print(f"User request_started: {sender}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")

@receiver(request_finished)
def on_request_finished(sender, **kwargs):
  print(f"User request_finished: {sender}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")

@receiver(got_request_exception)
def on_request_exception(sender, **kwargs):
  print(f"User got_request_exception: {sender}")
  print(f"sender : {sender}")
  print(f"kwargs : {kwargs}")

@receiver(connection_created)
def on_connection_created(sender, connection, **kwargs):
  print(f"User connection_created: {sender}")
  print(f"sender : {sender}")
  print(f" conenction : {connection}")
  print(f"kwargs : {kwargs}")