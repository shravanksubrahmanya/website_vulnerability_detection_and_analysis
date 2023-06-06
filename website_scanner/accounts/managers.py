from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, fname, lname, email, password):
        if not email:
            raise ValueError('User must provide valid email address')
        if not password:
            raise ValueError('User must provide password')
        if not fname:
            raise ValueError('User must provide first name')
        
        user = self.model(
            fname = fname,
            lname = lname,
            username = username,
            email = self.normalize_email(email=email), # it normalizes the email for storage
        )

        user.set_password(raw_password = password) # it hashes password before setting it up into the database
        user.save(using = self._db)
        return user

    
    def create_superuser(self, username, fname, lname, email, password):
        user = self.create_user(
            fname = fname,
            lname = lname,
            username= username,
            email=email, 
            password= password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user