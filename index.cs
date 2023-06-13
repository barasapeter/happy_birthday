using Android.App;
using Android.OS;
using Android.Widget;

namespace MyApp
{
    {
    [Activity(Label = "Hey Peter, it\'s your birthday!", MainLauncher = true)]
    public class MainActivity : Activity
    {
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            SetContentView(Resource.Layout.activity_main);

            LinearLayout linearLayout = new LinearLayout(this);
            linearLayout.Orientation = Orientation.Vertical;

            Button myButton = new Button(this);
            myButton.Text = "View your presents";
            myButton.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);
            myButton.Click += MyButton_Click;

            ImageView myImage = new ImageView(this);
            myImage.SetImageResource(Resource.Drawable.my_image);
            myImage.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);

            TextView myText = new TextView(this);
            myText.Text = "CONGRATULATIONS BARASA!";
            myText.TextSize = 24;
            myText.Gravity = Android.Views.GravityFlags.Center;
            myText.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);

            CheckBox myCheckbox = new CheckBox(this);
            myCheckbox.Text = "CONGRATULATIONS, BARASA!";
            myCheckbox.CheckedChange += MyCheckbox_CheckedChange;
            myCheckbox.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);

            linearLayout.AddView(myButton);
            linearLayout.AddView(myImage);
            linearLayout.AddView(myText);
            linearLayout.AddView(myCheckbox);

            SetContentView(linearLayout);
        }

        private void MyButton_Click(object sender, System.EventArgs e)
        {
            Toast.MakeText(this, "View your presents", ToastLength.Short).Show();
        }

        private void MyCheckbox_CheckedChange(object sender, CompoundButton.CheckedChangeEventArgs e)
        {
            if (e.IsChecked)
            {
                Toast.MakeText(this, "HAPPY BITHDAY!", ToastLength.Short).Show();
            }
            else
            {
                Toast.MakeText(this, "Checkbox unchecked!", ToastLength.Short).Show();
            }
        }
    }
}

    [Activity(Label = "MyApp", MainLauncher = true)]
    public class MainActivity : Activity
    {
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            SetContentView(Resource.Layout.activity_main);

            Button myButton = new Button(this);
            myButton.Text = "Click Me";
            myButton.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);

            ImageView myImage = new ImageView(this);
            myImage.SetImageResource(Resource.Drawable.my_image);
            myImage.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);

            LinearLayout linearLayout = new LinearLayout(this);
            linearLayout.Orientation = Orientation.Vertical;
            linearLayout.AddView(myButton);
            linearLayout.AddView(myImage);

            SetContentView(linearLayout);
        }
    }
}

namespace Picture
{
    [Activity(Label = "MyApp", MainLauncher = true)]
    public class MainActivity : Activity
    {
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            SetContentView(Resource.Layout.activity_main);

            LinearLayout linearLayout = new LinearLayout(this);
            linearLayout.Orientation = Orientation.Vertical;

            Button myButton = new Button(this);
            myButton.Text = "Click Me";
            myButton.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);
            myButton.Click += MyButton_Click;

            ImageView myImage = new ImageView(this);
            myImage.SetImageResource(Resource.Drawable.my_image);
            myImage.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);

            TextView myText = new TextView(this);
            myText.Text = "Hello, Android!";
            myText.TextSize = 24;
            myText.Gravity = Android.Views.GravityFlags.Center;
            myText.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);

            CheckBox myCheckbox = new CheckBox(this);
            myCheckbox.Text = "Check me";
            myCheckbox.CheckedChange += MyCheckbox_CheckedChange;
            myCheckbox.LayoutParameters = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WrapContent,
                LinearLayout.LayoutParams.WrapContent);

            linearLayout.AddView(myButton);
            linearLayout.AddView(myImage);
            linearLayout.AddView(myText);
            linearLayout.AddView(myCheckbox);

            SetContentView(linearLayout);
        }

        private void MyButton_Click(object sender, System.EventArgs e)
        {
            Toast.MakeText(this, "Button clicked!", ToastLength.Short).Show();
        }

        private void MyCheckbox_CheckedChange(object sender, CompoundButton.CheckedChangeEventArgs e)
        {
            if (e.IsChecked)
            {
                Toast.MakeText(this, "Checkbox checked!", ToastLength.Short).Show();
            }
            else
            {
                Toast.MakeText(this, "Checkbox unchecked!", ToastLength.Short).Show();
            }
        }
    }
}

