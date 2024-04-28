import diy_vector as v

def main():
    # image dimmensions
    image_width = 2560
    image_height = 256
    # file write
    output_file = open("output.ppm","w")
    output_file.write("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")
    # Render loops
    for j in range(0,image_height):
        print("Scanlines Remaining:" + str(image_height - j))
        for i in range(0, image_width):
            # set color value based on position
            # r = (i*2)/(image_width-1)     # whoops
            # g = (j*2)/(image_height-1)    # this looks kinda cool though
            r = i/(image_width-1)
            g = j/(image_height-1)
            b = 0
            # convert for file output
            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)
            output_file.write(str(ir) + " " + str(ig) + " " + str(ib) + "\n")
    output_file.close()
    print("Render complete.")



#main()
v.unit_test()