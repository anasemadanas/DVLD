namespace DVLD_System.UserControl
{
    partial class ucTakeTests
    {
        /// <summary> 
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.grpResult = new DevExpress.XtraEditors.GroupControl();
            this.radFail = new System.Windows.Forms.RadioButton();
            this.radPass = new System.Windows.Forms.RadioButton();
            this.picResult = new DevExpress.XtraEditors.PictureEdit();
            this.lblNotes = new DevExpress.XtraEditors.LabelControl();
            this.lblNotes1 = new DevExpress.XtraEditors.LabelControl();
            this.picNotes = new DevExpress.XtraEditors.PictureEdit();
            this.lblResult = new DevExpress.XtraEditors.LabelControl();
            this.btnSave = new DevExpress.XtraEditors.SimpleButton();
            this.btnClose = new DevExpress.XtraEditors.SimpleButton();
            this.lblScheduledTest = new DevExpress.XtraEditors.LabelControl();
            this.picVisionTest = new DevExpress.XtraEditors.PictureEdit();
            this.grpVisionTest = new DevExpress.XtraEditors.GroupControl();
            this.lblTestID = new DevExpress.XtraEditors.LabelControl();
            this.lblFees = new DevExpress.XtraEditors.LabelControl();
            this.lblTestID1 = new DevExpress.XtraEditors.LabelControl();
            this.lblFineFees = new DevExpress.XtraEditors.LabelControl();
            this.picTestID = new DevExpress.XtraEditors.PictureEdit();
            this.picTrial = new DevExpress.XtraEditors.PictureEdit();
            this.lblClass1 = new DevExpress.XtraEditors.LabelControl();
            this.lblName1 = new DevExpress.XtraEditors.LabelControl();
            this.lblName = new DevExpress.XtraEditors.LabelControl();
            this.lblAppID1 = new DevExpress.XtraEditors.LabelControl();
            this.picName = new DevExpress.XtraEditors.PictureEdit();
            this.lblClass = new DevExpress.XtraEditors.LabelControl();
            this.picFees = new DevExpress.XtraEditors.PictureEdit();
            this.lblFees1 = new DevExpress.XtraEditors.LabelControl();
            this.lblDate1 = new DevExpress.XtraEditors.LabelControl();
            this.picDate = new DevExpress.XtraEditors.PictureEdit();
            this.lblDate = new DevExpress.XtraEditors.LabelControl();
            this.lblTrial = new DevExpress.XtraEditors.LabelControl();
            this.lblTrial1 = new DevExpress.XtraEditors.LabelControl();
            this.picClass = new DevExpress.XtraEditors.PictureEdit();
            this.picAppID = new DevExpress.XtraEditors.PictureEdit();
            this.labelControl2 = new DevExpress.XtraEditors.LabelControl();
            ((System.ComponentModel.ISupportInitialize)(this.grpResult)).BeginInit();
            this.grpResult.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picResult.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picNotes.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVisionTest.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.grpVisionTest)).BeginInit();
            this.grpVisionTest.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picTestID.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTrial.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picName.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picFees.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picDate.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picClass.Properties)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picAppID.Properties)).BeginInit();
            this.SuspendLayout();
            // 
            // grpResult
            // 
            this.grpResult.Controls.Add(this.radFail);
            this.grpResult.Controls.Add(this.radPass);
            this.grpResult.Controls.Add(this.picResult);
            this.grpResult.Controls.Add(this.lblNotes);
            this.grpResult.Controls.Add(this.lblNotes1);
            this.grpResult.Controls.Add(this.picNotes);
            this.grpResult.Controls.Add(this.lblResult);
            this.grpResult.Location = new System.Drawing.Point(15, 382);
            this.grpResult.Name = "grpResult";
            this.grpResult.Size = new System.Drawing.Size(472, 152);
            this.grpResult.TabIndex = 125;
            // 
            // radFail
            // 
            this.radFail.AutoSize = true;
            this.radFail.Font = new System.Drawing.Font("Tahoma", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.radFail.Location = new System.Drawing.Point(216, 32);
            this.radFail.Name = "radFail";
            this.radFail.Size = new System.Drawing.Size(51, 23);
            this.radFail.TabIndex = 125;
            this.radFail.TabStop = true;
            this.radFail.Text = "Fail";
            this.radFail.UseVisualStyleBackColor = true;
            // 
            // radPass
            // 
            this.radPass.AutoSize = true;
            this.radPass.Font = new System.Drawing.Font("Tahoma", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.radPass.Location = new System.Drawing.Point(144, 32);
            this.radPass.Name = "radPass";
            this.radPass.Size = new System.Drawing.Size(58, 23);
            this.radPass.TabIndex = 124;
            this.radPass.TabStop = true;
            this.radPass.Text = "Pass";
            this.radPass.UseVisualStyleBackColor = true;
            // 
            // picResult
            // 
            this.picResult.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picResult.EditValue = global::DVLD_System.Properties.Resources.icoNational;
            this.picResult.Location = new System.Drawing.Point(80, 40);
            this.picResult.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picResult.Name = "picResult";
            this.picResult.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picResult.Properties.Appearance.Options.UseBackColor = true;
            this.picResult.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picResult.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picResult.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picResult.Size = new System.Drawing.Size(32, 24);
            this.picResult.TabIndex = 123;
            // 
            // lblNotes
            // 
            this.lblNotes.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblNotes.Appearance.Options.UseFont = true;
            this.lblNotes.Location = new System.Drawing.Point(16, 80);
            this.lblNotes.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblNotes.Name = "lblNotes";
            this.lblNotes.Size = new System.Drawing.Size(46, 20);
            this.lblNotes.TabIndex = 121;
            this.lblNotes.Text = "Notes:";
            // 
            // lblNotes1
            // 
            this.lblNotes1.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblNotes1.Appearance.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.lblNotes1.Appearance.Options.UseFont = true;
            this.lblNotes1.Appearance.Options.UseForeColor = true;
            this.lblNotes1.AutoSizeMode = DevExpress.XtraEditors.LabelAutoSizeMode.None;
            this.lblNotes1.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.Simple;
            this.lblNotes1.Location = new System.Drawing.Point(120, 64);
            this.lblNotes1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblNotes1.Name = "lblNotes1";
            this.lblNotes1.Size = new System.Drawing.Size(344, 80);
            this.lblNotes1.TabIndex = 122;
            // 
            // picNotes
            // 
            this.picNotes.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picNotes.EditValue = global::DVLD_System.Properties.Resources.icoNotes;
            this.picNotes.Location = new System.Drawing.Point(80, 72);
            this.picNotes.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picNotes.Name = "picNotes";
            this.picNotes.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picNotes.Properties.Appearance.Options.UseBackColor = true;
            this.picNotes.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picNotes.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picNotes.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picNotes.Size = new System.Drawing.Size(24, 24);
            this.picNotes.TabIndex = 120;
            // 
            // lblResult
            // 
            this.lblResult.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblResult.Appearance.Options.UseFont = true;
            this.lblResult.Location = new System.Drawing.Point(16, 40);
            this.lblResult.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblResult.Name = "lblResult";
            this.lblResult.Size = new System.Drawing.Size(50, 20);
            this.lblResult.TabIndex = 119;
            this.lblResult.Text = "Result:";
            // 
            // btnSave
            // 
            this.btnSave.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnSave.Appearance.ForeColor = System.Drawing.Color.Blue;
            this.btnSave.Appearance.Options.UseFont = true;
            this.btnSave.Appearance.Options.UseForeColor = true;
            this.btnSave.AppearanceHovered.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.btnSave.AppearanceHovered.Options.UseForeColor = true;
            this.btnSave.ImageOptions.Image = global::DVLD_System.Properties.Resources.icoSave;
            this.btnSave.Location = new System.Drawing.Point(372, 542);
            this.btnSave.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(112, 41);
            this.btnSave.TabIndex = 124;
            this.btnSave.Text = "Save";
            // 
            // btnClose
            // 
            this.btnClose.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnClose.Appearance.ForeColor = System.Drawing.Color.Blue;
            this.btnClose.Appearance.Options.UseFont = true;
            this.btnClose.Appearance.Options.UseForeColor = true;
            this.btnClose.AppearanceHovered.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.btnClose.AppearanceHovered.Options.UseForeColor = true;
            this.btnClose.ImageOptions.Image = global::DVLD_System.Properties.Resources.icoClose;
            this.btnClose.Location = new System.Drawing.Point(252, 542);
            this.btnClose.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.btnClose.Name = "btnClose";
            this.btnClose.Size = new System.Drawing.Size(112, 41);
            this.btnClose.TabIndex = 123;
            this.btnClose.Text = "Close";
            // 
            // lblScheduledTest
            // 
            this.lblScheduledTest.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblScheduledTest.Appearance.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(64)))), ((int)(((byte)(0)))));
            this.lblScheduledTest.Appearance.Options.UseFont = true;
            this.lblScheduledTest.Appearance.Options.UseForeColor = true;
            this.lblScheduledTest.Location = new System.Drawing.Point(148, 70);
            this.lblScheduledTest.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblScheduledTest.Name = "lblScheduledTest";
            this.lblScheduledTest.Size = new System.Drawing.Size(235, 37);
            this.lblScheduledTest.TabIndex = 122;
            this.lblScheduledTest.Text = "Scheduled Test";
            // 
            // picVisionTest
            // 
            this.picVisionTest.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picVisionTest.EditValue = global::DVLD_System.Properties.Resources.imgVision;
            this.picVisionTest.Location = new System.Drawing.Point(212, 11);
            this.picVisionTest.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picVisionTest.Name = "picVisionTest";
            this.picVisionTest.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picVisionTest.Properties.Appearance.Options.UseBackColor = true;
            this.picVisionTest.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picVisionTest.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picVisionTest.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picVisionTest.Size = new System.Drawing.Size(112, 51);
            this.picVisionTest.TabIndex = 121;
            // 
            // grpVisionTest
            // 
            this.grpVisionTest.AppearanceCaption.Font = new System.Drawing.Font("Tahoma", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.grpVisionTest.AppearanceCaption.Options.UseFont = true;
            this.grpVisionTest.Controls.Add(this.lblTestID);
            this.grpVisionTest.Controls.Add(this.lblFees);
            this.grpVisionTest.Controls.Add(this.lblTestID1);
            this.grpVisionTest.Controls.Add(this.lblFineFees);
            this.grpVisionTest.Controls.Add(this.picTestID);
            this.grpVisionTest.Controls.Add(this.picTrial);
            this.grpVisionTest.Controls.Add(this.lblClass1);
            this.grpVisionTest.Controls.Add(this.lblName1);
            this.grpVisionTest.Controls.Add(this.lblName);
            this.grpVisionTest.Controls.Add(this.lblAppID1);
            this.grpVisionTest.Controls.Add(this.picName);
            this.grpVisionTest.Controls.Add(this.lblClass);
            this.grpVisionTest.Controls.Add(this.picFees);
            this.grpVisionTest.Controls.Add(this.lblFees1);
            this.grpVisionTest.Controls.Add(this.lblDate1);
            this.grpVisionTest.Controls.Add(this.picDate);
            this.grpVisionTest.Controls.Add(this.lblDate);
            this.grpVisionTest.Controls.Add(this.lblTrial);
            this.grpVisionTest.Controls.Add(this.lblTrial1);
            this.grpVisionTest.Controls.Add(this.picClass);
            this.grpVisionTest.Controls.Add(this.picAppID);
            this.grpVisionTest.Controls.Add(this.labelControl2);
            this.grpVisionTest.Location = new System.Drawing.Point(12, 110);
            this.grpVisionTest.Name = "grpVisionTest";
            this.grpVisionTest.Size = new System.Drawing.Size(475, 264);
            this.grpVisionTest.TabIndex = 120;
            this.grpVisionTest.Text = "Vision Test";
            // 
            // lblTestID
            // 
            this.lblTestID.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTestID.Appearance.Options.UseFont = true;
            this.lblTestID.Location = new System.Drawing.Point(16, 232);
            this.lblTestID.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblTestID.Name = "lblTestID";
            this.lblTestID.Size = new System.Drawing.Size(56, 20);
            this.lblTestID.TabIndex = 108;
            this.lblTestID.Text = "Test ID:";
            // 
            // lblFees
            // 
            this.lblFees.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblFees.Appearance.Options.UseFont = true;
            this.lblFees.Location = new System.Drawing.Point(16, 200);
            this.lblFees.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblFees.Name = "lblFees";
            this.lblFees.Size = new System.Drawing.Size(40, 20);
            this.lblFees.TabIndex = 107;
            this.lblFees.Text = "Fees:";
            // 
            // lblTestID1
            // 
            this.lblTestID1.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTestID1.Appearance.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.lblTestID1.Appearance.Options.UseFont = true;
            this.lblTestID1.Appearance.Options.UseForeColor = true;
            this.lblTestID1.AutoSizeMode = DevExpress.XtraEditors.LabelAutoSizeMode.None;
            this.lblTestID1.Location = new System.Drawing.Point(152, 232);
            this.lblTestID1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblTestID1.Name = "lblTestID1";
            this.lblTestID1.Size = new System.Drawing.Size(112, 20);
            this.lblTestID1.TabIndex = 105;
            this.lblTestID1.Text = "???";
            // 
            // lblFineFees
            // 
            this.lblFineFees.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblFineFees.Appearance.Options.UseFont = true;
            this.lblFineFees.Location = new System.Drawing.Point(-96, 120);
            this.lblFineFees.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblFineFees.Name = "lblFineFees";
            this.lblFineFees.Size = new System.Drawing.Size(75, 20);
            this.lblFineFees.TabIndex = 104;
            this.lblFineFees.Text = "Fine Fees:";
            // 
            // picTestID
            // 
            this.picTestID.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picTestID.EditValue = global::DVLD_System.Properties.Resources.icoNational;
            this.picTestID.Location = new System.Drawing.Point(104, 232);
            this.picTestID.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picTestID.Name = "picTestID";
            this.picTestID.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picTestID.Properties.Appearance.Options.UseBackColor = true;
            this.picTestID.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picTestID.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picTestID.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picTestID.Size = new System.Drawing.Size(32, 24);
            this.picTestID.TabIndex = 106;
            // 
            // picTrial
            // 
            this.picTrial.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picTrial.EditValue = global::DVLD_System.Properties.Resources.icoCount;
            this.picTrial.Location = new System.Drawing.Point(104, 136);
            this.picTrial.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picTrial.Name = "picTrial";
            this.picTrial.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picTrial.Properties.Appearance.Options.UseBackColor = true;
            this.picTrial.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picTrial.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picTrial.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picTrial.Size = new System.Drawing.Size(32, 24);
            this.picTrial.TabIndex = 100;
            // 
            // lblClass1
            // 
            this.lblClass1.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblClass1.Appearance.Options.UseFont = true;
            this.lblClass1.Location = new System.Drawing.Point(152, 72);
            this.lblClass1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblClass1.Name = "lblClass1";
            this.lblClass1.Size = new System.Drawing.Size(27, 20);
            this.lblClass1.TabIndex = 99;
            this.lblClass1.Text = "???";
            // 
            // lblName1
            // 
            this.lblName1.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblName1.Appearance.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.lblName1.Appearance.Options.UseFont = true;
            this.lblName1.Appearance.Options.UseForeColor = true;
            this.lblName1.AutoSizeMode = DevExpress.XtraEditors.LabelAutoSizeMode.None;
            this.lblName1.Location = new System.Drawing.Point(152, 104);
            this.lblName1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblName1.Name = "lblName1";
            this.lblName1.Size = new System.Drawing.Size(240, 20);
            this.lblName1.TabIndex = 98;
            this.lblName1.Text = "???";
            // 
            // lblName
            // 
            this.lblName.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblName.Appearance.Options.UseFont = true;
            this.lblName.Location = new System.Drawing.Point(16, 104);
            this.lblName.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblName.Name = "lblName";
            this.lblName.Size = new System.Drawing.Size(46, 20);
            this.lblName.TabIndex = 97;
            this.lblName.Text = "Name:";
            // 
            // lblAppID1
            // 
            this.lblAppID1.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblAppID1.Appearance.Options.UseFont = true;
            this.lblAppID1.Location = new System.Drawing.Point(152, 40);
            this.lblAppID1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblAppID1.Name = "lblAppID1";
            this.lblAppID1.Size = new System.Drawing.Size(27, 20);
            this.lblAppID1.TabIndex = 96;
            this.lblAppID1.Text = "???";
            // 
            // picName
            // 
            this.picName.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picName.EditValue = global::DVLD_System.Properties.Resources.icoPerson;
            this.picName.Location = new System.Drawing.Point(104, 104);
            this.picName.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picName.Name = "picName";
            this.picName.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picName.Properties.Appearance.Options.UseBackColor = true;
            this.picName.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picName.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picName.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picName.Size = new System.Drawing.Size(32, 24);
            this.picName.TabIndex = 95;
            // 
            // lblClass
            // 
            this.lblClass.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblClass.Appearance.Options.UseFont = true;
            this.lblClass.Location = new System.Drawing.Point(16, 72);
            this.lblClass.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblClass.Name = "lblClass";
            this.lblClass.Size = new System.Drawing.Size(63, 20);
            this.lblClass.TabIndex = 92;
            this.lblClass.Text = "D. Class:";
            // 
            // picFees
            // 
            this.picFees.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picFees.EditValue = global::DVLD_System.Properties.Resources.icoMoney;
            this.picFees.Location = new System.Drawing.Point(104, 200);
            this.picFees.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picFees.Name = "picFees";
            this.picFees.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picFees.Properties.Appearance.Options.UseBackColor = true;
            this.picFees.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picFees.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picFees.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picFees.Size = new System.Drawing.Size(32, 24);
            this.picFees.TabIndex = 94;
            // 
            // lblFees1
            // 
            this.lblFees1.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblFees1.Appearance.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.lblFees1.Appearance.Options.UseFont = true;
            this.lblFees1.Appearance.Options.UseForeColor = true;
            this.lblFees1.AutoSizeMode = DevExpress.XtraEditors.LabelAutoSizeMode.None;
            this.lblFees1.Location = new System.Drawing.Point(152, 200);
            this.lblFees1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblFees1.Name = "lblFees1";
            this.lblFees1.Size = new System.Drawing.Size(152, 20);
            this.lblFees1.TabIndex = 93;
            this.lblFees1.Text = "???";
            // 
            // lblDate1
            // 
            this.lblDate1.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblDate1.Appearance.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.lblDate1.Appearance.Options.UseFont = true;
            this.lblDate1.Appearance.Options.UseForeColor = true;
            this.lblDate1.AutoSizeMode = DevExpress.XtraEditors.LabelAutoSizeMode.None;
            this.lblDate1.Location = new System.Drawing.Point(152, 168);
            this.lblDate1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblDate1.Name = "lblDate1";
            this.lblDate1.Size = new System.Drawing.Size(128, 20);
            this.lblDate1.TabIndex = 91;
            this.lblDate1.Text = "???";
            // 
            // picDate
            // 
            this.picDate.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picDate.EditValue = global::DVLD_System.Properties.Resources.icoDateOfBirth;
            this.picDate.Location = new System.Drawing.Point(104, 168);
            this.picDate.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picDate.Name = "picDate";
            this.picDate.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picDate.Properties.Appearance.Options.UseBackColor = true;
            this.picDate.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picDate.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picDate.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picDate.Size = new System.Drawing.Size(32, 24);
            this.picDate.TabIndex = 90;
            // 
            // lblDate
            // 
            this.lblDate.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblDate.Appearance.Options.UseFont = true;
            this.lblDate.Location = new System.Drawing.Point(16, 168);
            this.lblDate.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblDate.Name = "lblDate";
            this.lblDate.Size = new System.Drawing.Size(39, 20);
            this.lblDate.TabIndex = 89;
            this.lblDate.Text = "Date:";
            // 
            // lblTrial
            // 
            this.lblTrial.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTrial.Appearance.Options.UseFont = true;
            this.lblTrial.Location = new System.Drawing.Point(16, 136);
            this.lblTrial.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblTrial.Name = "lblTrial";
            this.lblTrial.Size = new System.Drawing.Size(33, 20);
            this.lblTrial.TabIndex = 88;
            this.lblTrial.Text = "Trial:";
            // 
            // lblTrial1
            // 
            this.lblTrial1.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTrial1.Appearance.Options.UseFont = true;
            this.lblTrial1.Location = new System.Drawing.Point(152, 136);
            this.lblTrial1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.lblTrial1.Name = "lblTrial1";
            this.lblTrial1.Size = new System.Drawing.Size(27, 20);
            this.lblTrial1.TabIndex = 78;
            this.lblTrial1.Text = "???";
            // 
            // picClass
            // 
            this.picClass.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picClass.EditValue = global::DVLD_System.Properties.Resources.icoLicenseType;
            this.picClass.Location = new System.Drawing.Point(104, 72);
            this.picClass.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picClass.Name = "picClass";
            this.picClass.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picClass.Properties.Appearance.Options.UseBackColor = true;
            this.picClass.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picClass.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picClass.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picClass.Size = new System.Drawing.Size(32, 24);
            this.picClass.TabIndex = 74;
            // 
            // picAppID
            // 
            this.picAppID.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.picAppID.EditValue = global::DVLD_System.Properties.Resources.icoNational;
            this.picAppID.Location = new System.Drawing.Point(104, 40);
            this.picAppID.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.picAppID.Name = "picAppID";
            this.picAppID.Properties.Appearance.BackColor = System.Drawing.Color.Transparent;
            this.picAppID.Properties.Appearance.Options.UseBackColor = true;
            this.picAppID.Properties.BorderStyle = DevExpress.XtraEditors.Controls.BorderStyles.NoBorder;
            this.picAppID.Properties.ShowCameraMenuItem = DevExpress.XtraEditors.Controls.CameraMenuItemVisibility.Auto;
            this.picAppID.Properties.SizeMode = DevExpress.XtraEditors.Controls.PictureSizeMode.Stretch;
            this.picAppID.Size = new System.Drawing.Size(32, 24);
            this.picAppID.TabIndex = 73;
            // 
            // labelControl2
            // 
            this.labelControl2.Appearance.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelControl2.Appearance.Options.UseFont = true;
            this.labelControl2.Location = new System.Drawing.Point(16, 40);
            this.labelControl2.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.labelControl2.Name = "labelControl2";
            this.labelControl2.Size = new System.Drawing.Size(83, 20);
            this.labelControl2.TabIndex = 50;
            this.labelControl2.Text = "D.L.App ID:";
            // 
            // ucTakeTests
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.grpResult);
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.btnClose);
            this.Controls.Add(this.lblScheduledTest);
            this.Controls.Add(this.picVisionTest);
            this.Controls.Add(this.grpVisionTest);
            this.Name = "ucTakeTests";
            this.Size = new System.Drawing.Size(499, 595);
            ((System.ComponentModel.ISupportInitialize)(this.grpResult)).EndInit();
            this.grpResult.ResumeLayout(false);
            this.grpResult.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picResult.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picNotes.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVisionTest.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.grpVisionTest)).EndInit();
            this.grpVisionTest.ResumeLayout(false);
            this.grpVisionTest.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picTestID.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTrial.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picName.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picFees.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picDate.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picClass.Properties)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picAppID.Properties)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private DevExpress.XtraEditors.GroupControl grpResult;
        private System.Windows.Forms.RadioButton radFail;
        private System.Windows.Forms.RadioButton radPass;
        private DevExpress.XtraEditors.PictureEdit picResult;
        private DevExpress.XtraEditors.LabelControl lblNotes;
        private DevExpress.XtraEditors.LabelControl lblNotes1;
        private DevExpress.XtraEditors.PictureEdit picNotes;
        private DevExpress.XtraEditors.LabelControl lblResult;
        private DevExpress.XtraEditors.SimpleButton btnSave;
        private DevExpress.XtraEditors.SimpleButton btnClose;
        private DevExpress.XtraEditors.LabelControl lblScheduledTest;
        private DevExpress.XtraEditors.PictureEdit picVisionTest;
        private DevExpress.XtraEditors.GroupControl grpVisionTest;
        private DevExpress.XtraEditors.LabelControl lblTestID;
        private DevExpress.XtraEditors.LabelControl lblFees;
        private DevExpress.XtraEditors.LabelControl lblTestID1;
        private DevExpress.XtraEditors.LabelControl lblFineFees;
        private DevExpress.XtraEditors.PictureEdit picTestID;
        private DevExpress.XtraEditors.PictureEdit picTrial;
        private DevExpress.XtraEditors.LabelControl lblClass1;
        private DevExpress.XtraEditors.LabelControl lblName1;
        private DevExpress.XtraEditors.LabelControl lblName;
        private DevExpress.XtraEditors.LabelControl lblAppID1;
        private DevExpress.XtraEditors.PictureEdit picName;
        private DevExpress.XtraEditors.LabelControl lblClass;
        private DevExpress.XtraEditors.PictureEdit picFees;
        private DevExpress.XtraEditors.LabelControl lblFees1;
        private DevExpress.XtraEditors.LabelControl lblDate1;
        private DevExpress.XtraEditors.PictureEdit picDate;
        private DevExpress.XtraEditors.LabelControl lblDate;
        private DevExpress.XtraEditors.LabelControl lblTrial;
        private DevExpress.XtraEditors.LabelControl lblTrial1;
        private DevExpress.XtraEditors.PictureEdit picClass;
        private DevExpress.XtraEditors.PictureEdit picAppID;
        private DevExpress.XtraEditors.LabelControl labelControl2;
    }
}
