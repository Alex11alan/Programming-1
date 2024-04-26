import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SeaGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(32, 18)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(333, 72)
		self._label1.TabIndex = 0
		self._label1.Text = " Enter the number of tickets sold for each class of seats:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SeaGreen
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(32, 120)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(131, 36)
		self._label2.TabIndex = 1
		self._label2.Text = " Class A:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SeaGreen
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(32, 201)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(131, 36)
		self._label3.TabIndex = 2
		self._label3.Text = " Class B:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.SeaGreen
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(32, 281)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(131, 36)
		self._label4.TabIndex = 3
		self._label4.Text = " Class C:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(203, 120)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(162, 35)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(203, 201)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(162, 35)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(203, 281)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(162, 35)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.SeaGreen
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(428, 120)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(131, 36)
		self._label5.TabIndex = 9
		self._label5.Text = " Class A Total:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.SeaGreen
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(428, 201)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(131, 36)
		self._label6.TabIndex = 8
		self._label6.Text = " Class B Total:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.SeaGreen
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(428, 280)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(131, 36)
		self._label7.TabIndex = 7
		self._label7.Text = " Class C Total:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.SeaGreen
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(616, 119)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(131, 36)
		self._label8.TabIndex = 12
		self._label8.Text = " "
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.SeaGreen
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(616, 201)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(131, 36)
		self._label9.TabIndex = 11
		self._label9.Text = " "
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.SeaGreen
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(616, 281)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(131, 36)
		self._label10.TabIndex = 10
		self._label10.Text = " "
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.SeaGreen
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(203, 392)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(356, 111)
		self._label11.TabIndex = 13
		self._label11.Text = " "
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.SeaGreen
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(203, 356)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(356, 36)
		self._label12.TabIndex = 14
		self._label12.Text = " Total Revenue:"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(400, 18)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(114, 72)
		self._button1.TabIndex = 15
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(530, 18)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(114, 72)
		self._button2.TabIndex = 16
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(659, 18)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(114, 72)
		self._button3.TabIndex = 17
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SpringGreen
		self.ClientSize = System.Drawing.Size(794, 512)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Stadium Seating"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		
		classA = num1 * 15
		classB = num2 * 12
		classC = num3 * 9
		
		self._label8.Text = str(classA)
		self._label9.Text = str(classB)
		self._label10.Text = str(classC)
		self._label11.Text = str(classA + classB + classC)

	def Button2Click(self, sender, e):
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()