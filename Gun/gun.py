class Gun:
    def __init__(self, number_of_bullets: int, is_magazine_empty: bool):
        self.number_of_bullets = number_of_bullets
        self.is_magazine_empty = is_magazine_empty

    def check_empty(self):
        if self.number_of_bullets == 0:
            self.is_magazine_empty = True

        else:
            self.is_magazine_empty = False
        return self.is_magazine_empty

    def reload(self):
        if self.number_of_bullets >= 0 or self.number_of_bullets < 7:
            self.number_of_bullets += 1
        else:
            self.number_of_bullets = self.number_of_bullets

    def check_magazine(self):
        return self.number_of_bullets

    def shoot(self):
        if self.number_of_bullets > 0 or self.number_of_bullets <= 7:
            self.number_of_bullets -= 1
        else:
            self.number_of_bullets = self.number_of_bullets
