from faker import Faker

fake = Faker("en_US")


def generate_user():
    return {

        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "postal_code": fake.zipcode()

    }
