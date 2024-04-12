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
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSeaGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ControlText
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(247, 62)
		self._label1.TabIndex = 0
		self._label1.Text = "Guests:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSeaGreen
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ControlText
		self._label2.Location = System.Drawing.Point(12, 90)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(247, 62)
		self._label2.TabIndex = 1
		self._label2.Text = "Chairs:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSeaGreen
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ControlText
		self._label3.Location = System.Drawing.Point(12, 171)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(247, 62)
		self._label3.TabIndex = 3
		self._label3.Text = "Permutuations:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSeaGreen
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ControlText
		self._label4.Location = System.Drawing.Point(12, 251)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(247, 62)
		self._label4.TabIndex = 2
		self._label4.Text = "Guests standing:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(266, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(247, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(267, 99)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(247, 20)
		self._textBox2.TabIndex = 5
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSeaGreen
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.ControlText
		self._label5.Location = System.Drawing.Point(266, 171)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(247, 62)
		self._label5.TabIndex = 7
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSeaGreen
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ControlText
		self._label6.Location = System.Drawing.Point(266, 251)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(247, 62)
		self._label6.TabIndex = 6
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 330)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(164, 104)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(182, 330)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(171, 104)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(359, 330)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(164, 104)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(535, 446)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		g = self._textBox1.Text
		c = self._textBox2.Text
		s = int(g - c)
		self._label6.Text = s
		self._label5.text = ""

	def Button2Click(self, sender, e):
		self._label5.Text = ""
		self._label6.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()