from models.repositories import ProfileRepository

class ProfileController:
    __profile_repo = None

    def __init__(self, profile_repo: ProfileRepository):
        self.__profile_repo = profile_repo

    def create_profile(self, profile: Profile):
        return self.__profile_repo.create_profile(profile)

    def delete_profile(self, profile: Profile):
        return self.delete_profile(profile)

    def show_profile(self, profile: Profile):
        self.__profile_repo.show_profile(profile)

    def update_profile(self, profile: Profile):
        return self.__profile_repo.update_profile(profile)

    