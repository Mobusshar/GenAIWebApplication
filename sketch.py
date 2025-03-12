python run_painterly_render.py \
  -c diffsketcher.yaml \
  -eval_step 10 -save_step 10 \
  -update "token_ind=4 num_paths=96 num_iter=800" \
  -pt "a photo of Sydney opera house" \
  -respath ./workdir/sydney_opera_house \
  -d 8019 \
  --download
