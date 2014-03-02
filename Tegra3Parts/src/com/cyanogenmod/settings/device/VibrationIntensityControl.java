package com.cyanogenmod.settings.device;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.Preference;
import android.preference.Preference.OnPreferenceChangeListener;
import android.preference.PreferenceManager;

public class VibrationIntensityControl implements OnPreferenceChangeListener {

    private static final String FILE = "/sys/class/timed_output/vibrator/dutycycle";

    public static boolean isSupported() {
        return Utils.fileWritable(FILE);
    }

	public static String getValue(Context context) {
		String value = Utils.getFileValue(FILE, "35000");
        SharedPreferences sharedPrefs = PreferenceManager.getDefaultSharedPreferences(context);
        return sharedPrefs.getString(DeviceSettings.KEY_VIBRATION_INTENSITY, value);
	}
	
    /**
     * Restore Vibration Intensity setting from SharedPreferences. (Write to kernel.)
     * @param context       The context to read the SharedPreferences from
     */
    public static void restore(Context context) {
        if (!isSupported()) {
            return;
        }

		String value = getValue(context);
        Utils.writeValue(FILE, value);
    }

    @Override
    public boolean onPreferenceChange(Preference preference, Object newValue) {
        Utils.writeValue(FILE, (String) newValue);
        return true;
    }

}
