<div align="center">
    <h1>🫟</h1>
    <h2>Slopper</h2>
</div>


Slopper is a programming language compiled by an AI. **Instead of a standard compiler, an AI takes your code, rewrites it in assembly, and Slopper uses `as` and `ld` to
assemble that code.** This project is NOT meant for production, it is just a fun little thing I made because I was bored.

To run, clone the source and start:

```bash
python3 src/main.py
```

Try building the example:

```bash
python3 src/main.py build example_entry_point.slop
```

You will need a Cohere API key. Slopper will automatically ask for one and give instructions.

---

Slopper is very stable.

```
mostypc123@rr:~/slopper$ python src/main.py build example.slop
:: Building example.slop
checking for cohere api key... ok
sending code to ai...
  thinking: wrote 89 lines
/usr/bin/ld: warning: cannot find entry symbol _start; defaulting to 0000000000401000
Created output a.out!
mostypc123@rr:~/slopper$ ./a.out
Segmentation fault         ./a.out
mostypc123@rr:~/slopper$
```
