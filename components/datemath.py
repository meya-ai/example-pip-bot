from meya import Component
import pendulum


class DateMath(Component):

    def start(self):
        dt_toronto = pendulum.create(2012, 1, 1, tz='America/Toronto')
        dt_vancouver = pendulum.create(2012, 1, 1, tz='America/Vancouver')
        print(dt_vancouver.diff(dt_toronto).in_hours())
        return self.respond()
