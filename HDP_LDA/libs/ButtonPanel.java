
//
// 按钮容器Panel，放置了四个按钮
//

import java.awt.*;
import java.awt.event.*;
import java.io.*;

class ButtonPanel extends Panel implements ActionListener {

	Viewer viewer;
	Button disconnectButton;
	Button optionsButton;
	Button recordButton;
	Button clipboardButton;
	Button ctrlAltDelButton;
	Button refreshButton;
	Button ftpButton;

	ButtonPanel(Viewer v) {
		viewer = v;

		setLayout(new FlowLayout(FlowLayout.LEFT, 0, 0));
		if (v.ftpOnly) {
			disconnectButton = new Button("Quit");
		} else {
			disconnectButton = new Button("Close");
		}
		disconnectButton.setEnabled(false);
		add(disconnectButton);
		disconnectButton.addActionListener(this);
		if (!v.ftpOnly) {
			optionsButton = new Button("Options");
			add(optionsButton);
			optionsButton.addActionListener(this);
			clipboardButton = new Button("Clipboard");
			clipboardButton.setEnabled(false);
			add(clipboardButton);
			clipboardButton.addActionListener(this);
			if (viewer.rec != null) {
				recordButton = new Button("Record");
				add(recordButton);
				recordButton.addActionListener(this);
			}
			ctrlAltDelButton = new Button("Send Ctrl-Alt-Del");
			ctrlAltDelButton.setEnabled(false);
			add(ctrlAltDelButton);
			ctrlAltDelButton.addActionListener(this);
			refreshButton = new Button("Refresh");
			refreshButton.setEnabled(false);
			add(refreshButton);
			refreshButton.addActionListener(this);
		}
		ftpButton = new Button("File Transfer");
		ftpButton.setEnabled(false);
		add(ftpButton);
		ftpButton.addActionListener(this);
	}

	//
	// 连接成功以后开启按钮
	//

	public void enableButtons() {
		disconnectButton.setEnabled(true);
		ftpButton.setEnabled(true);
		if (viewer.ftpOnly) {return;}
		clipboardButton.setEnabled(true);
		refreshButton.setEnabled(true);
	}

	//
	// 断开连接以后关闭按钮
	//

	public void disableButtonsOnDisconnect() {
		ftpButton.setEnabled(false);
		if (viewer.ftpOnly) {return;}

		remove(disconnectButton);
		disconnectButton = new Button("Hide desktop");
		disconnectButton.setEnabled(true);
		add(disconnectButton, 0);
		disconnectButton.addActionListener(this);

		optionsButton.setEnabled(false);
		clipboardButton.setEnabled(false);
		ctrlAltDelButton.setEnabled(false);
		refreshButton.setEnabled(false);

		validate();
	}

	//
	// 开启/关闭访问控制按钮
	//

	public void enableRemoteAccessControls(boolean enable) {
		if (viewer.ftpOnly) {return;}
		ctrlAltDelButton.setEnabled(enable);
	}

	//
	// 事件处理函数
	//

	public void actionPerformed(ActionEvent evt) {

		viewer.moveFocusToDesktop();

		if (evt.getSource() == disconnectButton) {
			viewer.disconnect();

		} else if (evt.getSource() == optionsButton) {
			viewer.options.setVisible(!viewer.options.isVisible());

		} else if (evt.getSource() == recordButton) {
			viewer.rec.setVisible(!viewer.rec.isVisible());

		} else if (evt.getSource() == clipboardButton) {
			viewer.clipboard.setVisible(!viewer.clipboard.isVisible());

		} else if (evt.getSource() == ctrlAltDelButton) {
			try {
				final int modifiers = InputEvent.CTRL_MASK | InputEvent.ALT_MASK;

				KeyEvent ctrlAltDelEvent =
					new KeyEvent(this, KeyEvent.KEY_PRESSED, 0, modifiers, 127);
				viewer.rfb.writeKeyEvent(ctrlAltDelEvent);

				ctrlAltDelEvent =
					new KeyEvent(this, KeyEvent.KEY_RELEASED, 0, modifiers, 127);
				viewer.rfb.writeKeyEvent(ctrlAltDelEvent);

			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		else if (evt.getSource() == refreshButton)
		{
			try {
				RfbProto rfb = viewer.rfb;
				rfb.writeFramebufferUpdateRequest(0, 0, rfb.framebufferWidth,
						rfb.framebufferHeight, false);
			}
			catch (IOException e)
			{
				e.printStackTrace();
			}
		}
		else if (evt.getSource() == ftpButton)
		{
			//开始运行 
			if (viewer.ftpOnly) {
				viewer.vncFrame.setVisible(false);
			}
			viewer.ftp.setSavedLocations();
			if (viewer.ftp.isVisible()) {
				viewer.ftp.doClose();
			} else {
				viewer.ftp.doOpen();
			}
			//结束运行 
			viewer.rfb.readServerDriveList();
		}
	}
}

