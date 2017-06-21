import dxpy
import sys
import time


def runsimpleapp_getoutput(input_str, sleep_int):
    applet = dxpy.find_one_data_object(
                classname='applet',
                name='return_input_after_sleeping',
                project='project-F4Kv2280g45x6ZyFFj8FJgxZ',
                zero_ok=False,
                more_ok=False,
                return_handler=True)

    input_dict = {'input_str': input_str,
                  'sleep_int': sleep_int}
    run_obj = applet.run(input_dict)
    run_obj.wait_on_done()
    output = str(run_obj.describe()['output']['output_str'])
    return output


if __name__ == "__main__":
    input_str = sys.argv[1]
    sleep_int = int(sys.argv[2])
    outs = runsimpleapp_getoutput(input_str=input_str, sleep_int=sleep_int)
    print outs
