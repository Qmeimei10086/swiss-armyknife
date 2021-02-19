from flask import Flask, render_template,request
import ctypes
 
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
 
FOREGROUND_BLACK = 0x0
FOREGROUND_BLUE = 0x01  # text color contains blue.
FOREGROUND_GREEN = 0x02  # text color contains green.
FOREGROUND_RED = 0x04  # text color contains red.
FOREGROUND_INTENSITY = 0x08  # text color is intensified.
 
BACKGROUND_BLUE = 0x10  # background color contains blue.
BACKGROUND_GREEN = 0x20  # background color contains green.
BACKGROUND_RED = 0x40  # background color contains red.
BACKGROUND_INTENSITY = 0x80  # background color is intensified.
 
 
class Color:

    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
    def set_cmd_color(self, color, handle=std_out_handle):
        
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool
 
    def reset_color(self):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
 
    def print_red_text(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        print(print_text)
        self.reset_color()
 
    def print_green_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        print(print_text)
        self.reset_color()
 
    def print_blue_text(self, print_text):
        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        print(print_text)
        self.reset_color()
 
    def print_red_text_with_blue_bg(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY | BACKGROUND_BLUE | BACKGROUND_INTENSITY)
        print(print_text)
        self.reset_color()


app = Flask(__name__)
@app.route('/')
def sqlmapGUI():
    return render_template('server.html')

@app.route('/cmd',methods=['GET'])
def wait():
    print(request.url)
    fh = request.args.get('cmd')
    
    res = fh.replace('+',' ')
    
    clr = Color()
    
    print('                                                                                    ')
    clr.print_red_text('=======================================================================')
    clr.print_red_text(res)
    clr.print_red_text('=======================================================================')
    print('                                                                                    ')
    return 'ok'
def main():
    print('hello')
    app.run(host="0.0.0.0",port=8080)

if __name__ == "__main__":
    main()
