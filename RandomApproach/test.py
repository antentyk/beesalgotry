import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib.animation import ImageMagickFileWriter

from RandomApproach import RandomApproach
from functions import cross_in_tray
from Settings import Settings

# _____________
# WON'T WORK ON YOUR MACHINE UNLESS YOU INSTALL ImageMagick
# _____________

matplotlib.verbose.set_level("helpful")
plt.rcParams['animation.convert_path'] = 'C:\\Program Files\\ImageMagick-7.0.7-Q16\\magick.exe'
matplotlib.rcParams['animation.ffmpeg_path'] = 'C:\\ffmpeg\\bin\\ffmpeg.exe'

# _____________
# _____________
# _____________

r = RandomApproach(cross_in_tray,
                   Settings,
                   10**5,
                   10**3)

it = r.__iter__()

def animate(i):
    try:
        return it.__next__()
    except:
        return

# ___________
# SHOWING ANIMATION
# ___________

if(__name__ != '__main__'):
    ani = FuncAnimation(r.fig, animate, repeat=False, interval=2)
    plt.show()

# ___________
# SAVING TO GIF
# ___________

else:
    ani = FuncAnimation(r.fig, animate, repeat=False, interval=10, frames=100)
    ani.save('line.gif', writer=ImageMagickFileWriter())