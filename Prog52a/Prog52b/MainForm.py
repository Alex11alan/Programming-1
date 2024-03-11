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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(200, 27)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(48, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(368, 27)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(48, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(117, 27)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(48, 20)
		self._textBox3.TabIndex = 2
		self._textBox3.TextChanged
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(284, 27)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(48, 20)
		self._textBox4.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Thistle
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(34, 134)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(154, 42)
		self._label1.TabIndex = 5
		self._label1.Text = "Sum:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Thistle
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(34, 204)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(154, 42)
		self._label2.TabIndex = 6
		self._label2.Text = "Average:"
		
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(34, 307)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(142, 98)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(201, 307)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(142, 98)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(367, 307)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(142, 98)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Teal
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(337, 134)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(172, 42)
		self._label3.TabIndex = 10
		
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Teal
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(337, 204)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(172, 42)
		self._label4.TabIndex = 11
		
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(550, 435)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog52b"
		self.ResumeLayout(False)
		self.PerformLayout()
	
	def Button1Click(self, sender, e):
		variable1 = self._textBox1.Text
		variable2 = self._textBox2.Text
		variable3 = self._textBox3.Text
		variable4 = self._textBox4.Text
		sum = variable1 + variable2 + variable3 + variable4
		averge = sum / 4
		self._label3.Text = sum
		self._label4.Text = average

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		application.Exit()