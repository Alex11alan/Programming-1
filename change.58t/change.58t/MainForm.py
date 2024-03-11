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
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Cornsilk
		self._label1.Location = System.Drawing.Point(12, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(235, 59)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Cornsilk
		self._label2.Location = System.Drawing.Point(12, 101)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(235, 59)
		self._label2.TabIndex = 1
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Cornsilk
		self._label3.Location = System.Drawing.Point(411, 93)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(235, 59)
		self._label3.TabIndex = 3
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Cornsilk
		self._label4.Location = System.Drawing.Point(411, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(235, 59)
		self._label4.TabIndex = 2
		self._label4.Text = "label4"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(658, 634)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "change.58t"
		self.ResumeLayout(False)

