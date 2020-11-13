# devoloper guide
WARNING shutdown thing needed  
simply subclass `actor.Actor` after running `import actor` when actor.py is in a direcotry in your PYTHONPATH, override the `resolve_msg(self,msg)` method,to store persistent state use the self.state dict in `resolve_msg`,to exit use the `self.exit(exitcode)` method,instance your actor subclass,run `mqvar = actor_sub_class_instance.startactor()`, to trigger events use `mqvar.send`.  
full example:
```python3
import actor
class myactor(actor.Actor):
    def resolve_msg(self,msg):
        print(msg)
        if msg=="shutdown":
            self.exit("NORMAL")

x=myactor()
mq=x.startactor()
mq.send("Lorem ipsum dolor sit amet")
mq.send("shutdown")
```
