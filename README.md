
ดูเหมือนว่าคุณเรียกใช้สคริปต์สำเร็จแล้ว และกำลังแสดงเวลาทั้งหมดที่สคริปต์ Python ใช้longIO.pyในการดำเนินการ

คำtimeสั่งใน Unix/Linux ให้ผลลัพธ์ดังต่อไปนี้: python longIO.py 0.51s user 0.82s system 96% cpu 1.382 total. ซึ่งจะให้เวลาทั้งหมดสำหรับกระบวนการในการดำเนินการแก่คุณ:

0.51s user: นี่คือระยะเวลาของ CPU ที่กระบวนการใช้ในโหมดผู้ใช้
0.82s system: นี่คือระยะเวลาของ CPU ที่กระบวนการใช้ในโหมดเคอร์เนล
1.382 total: นี่คือเวลาทั้งหมดที่ผ่านไประหว่างการดำเนินการของกระบวนการ
ผลลัพธ์นี้ไม่เพียงแต่รวมถึงเวลาของการดำเนินการ I/O ของคุณ แต่ยังรวมถึงค่าใช้จ่ายอื่นๆ เช่น ตัวแปล Python ที่เริ่มต้นทำงาน การคอมไพล์สคริปต์ของคุณ และอื่นๆ เวลาจริงที่ใช้โดยการดำเนินการ I/O ของคุณควรมองเห็นได้ในผลลัพธ์ของสคริปต์ Python

อย่างที่คุณเห็น การดำเนินการ I/O ในการเขียนข้อมูลจำนวนมากลงในไฟล์จะใช้เวลามากกว่าการดำเนินการที่เชื่อมโยงกับ CPU ในการคำนวณตัวเลขฟีโบนัชชีจำนวนมาก สิ่งนี้แสดงให้เห็นว่าการดำเนินการ I/O นั้นช้ากว่าการทำงานของ CPU โดยเฉพาะอย่างยิ่งเมื่อต้องจัดการกับข้อมูลจำนวนมาก 
user time,0.51s user,

In UNIX and UNIX-like operating systems, the operating system kernel has two types of code: user mode and kernel mode. User mode is a restricted processing mode designed for applications, while kernel mode is a privileged processing mode designed for system code.

User mode: When your program is executing instructions (like adding two numbers or comparing values), it is operating in user mode.
Kernel mode: When your program needs to perform I/O operations or other system-level operations, it makes a system call, which switches execution to kernel mode.
In your case, 0.51s user means that the CPU spent 0.51 seconds executing your program's instructions in user mode. This includes things like preparing data to be written to the file and calculating Fibonacci numbers.

The 0.82s system time is the time the CPU spent executing system calls on behalf of your program, such as writing the data to the file.

This illustrates one reason why I/O operations are slower than pure CPU operations: they require system calls, which involve switching to kernel mode, which takes time.