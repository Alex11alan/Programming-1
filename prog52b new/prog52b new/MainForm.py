import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(117, 41)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(223, 41)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(329, 41)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(435, 41)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Magenta
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 133)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(168, 52)
		self._label1.TabIndex = 4
		self._label1.Text = " Sum:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Magenta
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 219)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(168, 52)
		self._label2.TabIndex = 5
		self._label2.Text = " Average:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Violet
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(472, 133)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(168, 52)
		self._label3.TabIndex = 6
		self._label3.Text = " "
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Violet
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(472, 219)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(168, 52)
		self._label4.TabIndex = 7
		self._label4.Text = " "
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 349)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(135, 67)
		self._button1.TabIndex = 8
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(153, 349)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(346, 67)
		self._button2.TabIndex = 9
		self._button2.Text = "Calculate "
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(505, 349)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(135, 67)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(652, 428)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog52b new"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		

	def Button2Click(self, sender, e):
		variable1 = int(self._textBox1.Text)
		variable2 = int(self._textBox2.Text)
		variable3 = int(self._textBox3.Text)
		variable4 = int(self._textBox4.Text)
		sum = variable1 + variable2 + variable3 + variable4
		average = sum / 4.00
		self._label3.Text = str(sum)
		self._label4.Text = str(average)
	

	def Button3Click(self, sender, e):
		Application.Exit()