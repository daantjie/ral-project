
class Adire:

    def __init__(self, eye, neck, tongue):
        self.eye = eye
        self.neck = neck
        self.tongue = tongue

    def run(self):
        data = self.scan()
        self.analyse(data)

    def scan(self, resolution=5):
        data = []
        while True:
            line = self.scanline(resolution)
            data.append(line)
            self.tongue.shift(resolution)
            if self.tongue.endp():
                line = self.scanline(resolution)
                data.append(line)
                break
        return data

    def scanline(self, resolution):
        line = []
        while True:
            line.append(self.eye.blackp())
            self.neck.shift(resolution)
            if self.neck.endp():
                line.append(self.eye.blackp())
                break
        if self.neck.backwardsp():
            line.reverse()
            self.neck.toggle_direction()
        return line
