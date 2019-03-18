import os
import sys
import time
from argparse import ArgumentParser
sys.path.append("./src")
from faceAverage import Averager


if __name__ == '__main__' :
    start = time.time()

    parser = ArgumentParser()
    parser.add_argument('-i', '--input-dir', dest="input", help="Specify the input directory", type=str, required=True)
    parser.add_argument('-ow', '--output-width', dest="width", help="Specify the output file width. Default 300", type=int, default=300)
    parser.add_argument('-oh', '--output-height', dest="height", help="Specify the output file height. Default 400", type=int, default=400)
    parser.add_argument('-e', '--extensions', dest="ext", help="Specify the file extensions like *.jpg *.whatevs.file", nargs="+")
    parser.add_argument('-o', '--output-path', dest="output", help="Specify the output path for writing result. Default ./results/[input-dir-names].jpg", type=str)
    parser.add_argument('-w', '--window', dest="window", help="Shows window if specified", action="store_true", default=False)
    parser.add_argument('-nw', '--no-warps', dest="noWarps", help="Hides warping stage if specified", action="store_true", default=False)
    parser.add_argument('-nc', '--no-caching', dest="noCaching", help="Ignores .ff file cache if specified", action="store_true", default=False)
    parser.add_argument('-wt', '--window-time', dest="windowTime", help="Duration of each frame in debug window", type=int, default=500)
    parser.add_argument('-t', '--template', dest="template", help="Template input image to set as the main face shape rather than the total average", type=str, default=None)

    options = parser.parse_args()
    print(options)
    ext = options.ext or ["*.jpg", "*.jpeg"]
    Averager(width=options.width, height=options.height).run(path=options.input, ext=ext, window=options.window, showWarps=not options.noWarps, windowTime=options.windowTime, useCaching=not options.noCaching, template=options.template).save(name=options.output)

    print(f">>> Executed in {time.time()-start:.2f} seconds")
