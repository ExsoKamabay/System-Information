from system_intelligence.query import *;
from art import *;from stringcolor import *;
from url64 import *;from random import choice;
from time import sleep as timeout;import os;
import animation;from shutil import rmtree;
class SystemInfo:
    def __init__(self):
        setattr(self,"xcolors",(choice(["#8A2BE2","#6495ED","#008B8B","#006400"])));
        setattr(self,"X00fjxd",(cs(text2art(decode("U1lTSQ"),"calgphy2",True,None),getattr(self,"xcolors"))));
        setattr(self,"dT970xB",([decor("wave2"),text2art(decode("U3lzdGVtIEluZm9ybWF0aW9u"),"lopioo",True,"wave2")]));
        setattr(self,"Exkmy07",(cs(text2art(decode("RXhzbyBLYW1hYmF5"),"lilia",True,"wave1"),getattr(self,"xcolors"))));
        setattr(self,"xdfgF70",(cs(
            decor("wave2",reverse=True)+getattr(self,"dT970xB")[1]+getattr(self,"dT970xB")[0],getattr(self,"xcolors")
        )));
    def req(self):
        os.system("pip3 install pycuda");
        os.system("apt install lshw");
    @animation.wait("bar")
    def loading(self):
        timeout(10);return;
    def xmain(self):
        query(query_scope=['all'],verbose=True);
    def main(self):
        print(
            getattr(self,"X00fjxd"),"\n\t    ",
            getattr(self,"Exkmy07"),"\n   ",
            getattr(self,"xdfgF70"),"\n");
        print(cs(text2art("Sedang membaca system!","fancy64",True,
        "arrow_wave2"),getattr(self,"xcolors")));self.loading();
        self.xmain();setattr(self,"x0r",cs("\n\n"+decor("fancy64")+
        decode("c2F2ZSBvdXRwdXQgW3llcy9ub10-IA"),getattr(self,"xcolors")));
        setattr(self,"U53",input(getattr(self,"x0r")));
        if not getattr(self,"U53") or getattr(self,"U53") == "no":pass;
        elif getattr(self,"U53") == str(decode("c2V0dXA")):self.req();
        elif getattr(self,"U53") == str(decode("aGVscA")):
            class Help_me(SystemInfo):
                def __init__(self,*args):
                    print(cs(args[0],"#6495ED"))
            Help_me("\n%s\n%s\n%s\n%s\n%s\n"%(
                decode("TmFtYSA6IFNZU0kgKFN5c3RlbSBJbmZvcm1hdGlvbiks"),
                decode("RW1haSBrb250cmlidXNpIDogbGV4eW9uZzY2QGdtYWlsLmNvbSw"),
                decode("R2l0aHViIDogaHR0cHM6Ly93d3cuZ2l0aHViLmNvbS9FeHNvS2FtYWJheSw"),
                decode("WW91VHViZSA6IGh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL2NoYW5uZWwvVUNDa0ZQV2JRYXFvblBjNTF1VmVLdnlnLA"),
                decode("Q29weXJpZ2h0IDogMTQxMDIwMjAg")));
        elif getattr(self,"U53") == str("yes"):
            rmtree("output");os.makedirs(str("output"));query_and_export(query_scope=list(('all',)),verbose=True,
            generate_html_table=False,export_format=str(decode("anNvbg")),output='output/system_info.json');
            print("\t"+cs(text2art(" successfully ","fancy64",True,"wave1"),getattr(self,"xcolors")));
        else:print(cs("KeyInvalid",getattr(self,"xcolors")));
__name__==SystemInfo().main();
