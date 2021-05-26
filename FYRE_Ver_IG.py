#!/usr/bin/env python
# encoding: UTF-8
#edit so that names, hometowns and images fit.






































































if __name__ == '__main__':
  try:
    #!/usr/bin/env python
    # encoding: UTF-8
    
    # Silence warnings
    import psychopy.logging
    psychopy.logging.console.setLevel(psychopy.logging.CRITICAL)
    
    import schizoidpy
    from schizoidpy import StimGroup, TriggerKey
    from psychopy.visual import TextStim, ImageStim, Rect, Circle
    from psychopy.visual.ratingscale import RatingScale
    from psychopy.core import CountdownTimer
    from random import random, lognormvariate, expovariate, sample
    from collections import Counter
    from cgi import escape
    from sys import argv
    
    par = dict((('committed', 'Fri Feb 22 14:01:45 2019 -0500'), ('deployed', 'Sat Feb 23 10:07:36 2019'), ('task_version', '51f11b7f67a422727851368261d30dda20489dad'), ('image_dir', 'images/'), ('debug', False), ('eeg', True))); import socket; par["fmri_mode"] = socket.gethostname() == "PSY-2HJ6HR2"; par["subject_portrait_path"] = "C:/subject.jpg" if socket.gethostname() in ["TRACLab-wr2", "TracLabWhisper2"] else "subject.jpg"; par["debug_log_dir"] = "output-fmri"   if par["fmri_mode"] else "output-eeg"    if socket.gethostname() in ["PSY-B4B80M2", "PSY-2S5XQP2"] else "output-age-15" if socket.gethostname() == "PsychA115WR" else "output"; par["output_path_fmt"] = "{}/survivor-{{subject}}.json".format(par["debug_log_dir"]); par["inpout32_addr"] = None if socket.gethostname() == "CAPLAB-Whisp2in" else 53328 if socket.gethostname() in ["StewsLab-PC", "TRACLab-wr2", "TracLabWhisper2"] else 57424 if socket.gethostname() in ["Kujawa-Task-D45KNSD2"] else 57360 if socket.gethostname() in ["PSYCH1457", "PSY-B4B80M2"] else 16376 if socket.gethostname() == "PSY-2S5XQP2" else 888; par["double_draw"] = socket.gethostname() == "CAPLAB-Whisp2in"; par["shrink_screen"] = socket.gethostname() in ["TRACLab-wr2", "TracLabWhisper2"]
    o = schizoidpy.Task(
        debug_log_dir = par['debug_log_dir'],
        send_actiview_trigger_codes = par['eeg'] and not par['fmri_mode'],
        inpout32_addr = par['inpout32_addr'],
        double_draw = par['double_draw'],
        button_radius = .12,
        okay_button_pos = (0, -.7),
        bg_color = 'black', fixation_cross_color = 'white')
    o.save('task_version', par['task_version'])
    
    # ------------------------------------------------------------
    # * Data
    # ------------------------------------------------------------
    
    portrait_dims = (144, 216)
    ages = map(str, [
        18, 18, 18,
        19, 19, 19,
        20, 20, 20,
        21, 21,
        22, 22])
    
    if par['fmri_mode']:
        male_fs = {'Steve', 'Cody', 'Kyle', 'Aiden', 'Jacob', 'Daniel', 'Nick'}
        extra_male_name = 'Rob'
        female_names = {'Addison', 'Holly', 'Rachel', 'Lauren', 'Jennifer', 'Molly', 'Jessica'}
        extra_female_name = 'Kelsey'
        male_portraits = {'vanderbilt-undergrad-fmri-m-{}.jpg'.format(i + 1) for i in range(7)}
        female_portraits = {'vanderbilt-undergrad-fmri-f-{}.jpg'.format(i + 1) for i in range(7)}
        schools = {'Kennesaw State University', 'University of Phoenix', 'Texas Tech University', 'Tulane University', 'Temple University', 'Drexel University', 'Boise State University', 'University of Delaware', 'Old Dominion University', 'Birmingham-Southern College', 'University of North Carolina at Chapel Hill', 'Wake Forest University', 'Yale University'}
        interests = {
            'fishing, reading, spending time with friends',
            'rock climbing, politics, nature',
            'design and music',
            'playing guitar and spending time with friends and family',
            'travel, art, literature',
            'chess, spending time with friends',
            'drawing and painting',
            'cooking, meeting new people',
            'singing, choreography',
            'travel and foreign languages',
            'volunteering, reading, Spanish',
            'public health, sculpting, working out',
            'running, baking, hanging out with friends'}
        polls = [
            ['Who is your favorite fictional character?',
                ["Harry potter", "Katniss Everdeen", "Iron Man", "Jim from The Office", "Groot", "Luke skywalker", "Atticus finch", "Hannibal lector", "Captain jack sparrow", "Jane Eyre", "Sherlock holmes", "Daenerys Targaryen"]],
            ['If you could be any animal, what kind of animal would you be?',
                ["Golden retriever", "Cat", "Beta fish", "Hummingbird", "Mountain lion", "Panther", "Water snake", "Giraffe", "Wild horse", "Beagle", "Hedgehog"]],
            ['What is your favorite thing about your college or university?',
                ["The people", "The food", "Interesting classes", "Being independent from my family", "How pretty campus is", "Cool organizations to get involved with", "Living in a dorm with my friends", "My friends", "Getting to figure out who I am and what I want", "I get to set my own schedule"]],
            ['If you could live in any time period, which would it be?',
                ["The future", "The wild west", "The 1960s", "the 80s", "Paris in the 1920s", "medieval France", "the renaissance", "ancient Greece", "the golden age of film in Hollywood"]],
            ['If you suddenly won a million dollars, what would be the first thing you bought with the money?',
                ["A really fancy car", "A private island", "A mansion", "A beach house for my parents", "puppies", "designer clothes", "a luxury apartment", "a jet ski"]]]
    else:
        male_names = {'Brandon', 'Tyler', 'Matt', 'Ryan', 'Alex', 'Connor', 'Zhitao'}
        us_male_names = {'Brandon', 'Tyler', 'Matt','Connor'}
        inter_male_names = {'Ryan', 'Alex','Zhitao'}
        extra_male_name = 'Zach'
        female_names = {'Taylor', 'Clare', 'Alice', 'Renee', 'Irene', 'Xiaoyu', 'Qingxin'}
        us_female_names = {'Taylor', 'Clare', 'Renee','Alice'}
        inter_female_names = {'Irene', 'Xiaoyu', 'Qingxin'}
        extra_female_name = 'Sarah'
    #edit this
        male_portraits = {'vanderbilt-undergrad-eeg-m-{}.jpg'.format(i + 1) for i in range(7)}
        female_portraits = {'vanderbilt-undergrad-eeg-f-{}.jpg'.format(i + 1) for i in range(7)}
        us_male_portraits = {'vanderbilt-undergrad-eeg-m-{}.jpg'.format(i + 1) for i in range(4)}
        inter_male_portraits = {'vanderbilt-undergrad-eeg-m-{}.jpg'.format(i + 1) for i in range(4,7)}
        us_female_portraits = {'vanderbilt-undergrad-eeg-f-{}.jpg'.format(i + 1) for i in range(4)}
        inter_female_portraits = {'vanderbilt-undergrad-eeg-f-{}.jpg'.format(i + 1) for i in range(4,7)}
        schools = {'Harvard University', 'Yale', 'Stanford University', 'Columbia University', 'Duke', 'University of virginia', 'UPenn', 'wake forest university', 'Tufts', 'Caltech', 'University of Michigan', 'Emory', 'Northwestern University', 'Massachusetts Institute of Technology'}
        hometown_us_male = {
        ('Pasadena, CA'),
        ('new york city'),
        ('Syracuse, NY'),
        ('chicago')}
        hometown_us_female = {
        ('Smyrna, NY'),
        ('Miami, FL'),
        ('Fort Collins, Colorado'),
        ('ft.worth')}
        hometown_int_male = {
        ('Guangzhou'),
        ('Hong Kong'),
        ('Shanghai'),
        ('Nanyang')}
        hometown_int_female = {
        ('Wuhan'),
        ('Nanjing'),
        ('Beijing')}
        interests = {
            'Social justice and public policy',
            'dogs',
            'playing guitar',
            'Hanging out with friends and family, cooking, reading',
            'Hiking, the outdoors',
            'camping and yoga',
            'Soccer, hiking, and relaxing with friends',
            'sketching, hiking',
            'gaming and tech',
            'Politics and environmental activism',
            'volunteering, traveling',
            'sketching, photography',
            'foreign languages, culture, public health',
            'rock climbing, running, nature',
        '   fitness, hanging out with friends'}
        polls = [
            ["What is your favorite movie?",
                {"Lady Bird", "Into the Spiderverse", "Avengers: Endgame", "Crazy Rich Asians", "Harry Potter and the Prisoner of Azkaban", "A clockwork orange", "the matrix", "la la land", "The Farewell", "Pulp Fiction", "The Lion King", "Eternal sunshine of the spotless mind"}],
            ["If money didn't matter, what would be your dream job?",
                {"Broadway singer", "Chef", "Travel agent", "food blogger", "Event planner", "Children's book illustrator", "Antique shop owner", "Architect", "Astronaut", "Chocolatier", "advice columnist"}],
            ["If you had a whole day to do whatever you wanted, what would you do?",
                {"Sleep", "Go for a run and then hang out with friends", "Go to the airport and get on a random flight to somewhere I've never been before", "Go visit my parents", "Sleep late and watch Netflix", "Go to a coffee shop and read", "Go to the beach", "Do yoga in the park and then cook dinner with friends", "Go to brunch with my friends", "Go on a hike somewhere new"}],
            ["What is your least favorite class?",
                {"Chem", "Biology", "Macro economics", "Physics II", "Medieval literature", "neuro", "Statistics", "Computer organization", "Calculus"}],
            ["If you could have dinner with any person, living or dead, who would it be?",
                {"Barack Obama", "Nelson Mandela", "spike lee", "Sami Liu", "Stephen King", "Beyonce", "John Oliver", "Mark Zuckerberg"}]]
        nationality = {}
        for p in male_names: 
            if p in inter_male_names:
                nationality[p] = 'international'
            else:
                nationality[p] = 'national'
        for p in female_names: 
            if p in inter_female_names:
                nationality[p] = 'international'
            else:
                nationality[p] = 'national'

    round_descriptions = [
        dict(place = 'Kauai',
            background = 'Hanalei,_Kauai_HI.jpg',
            fluff = "Welcome to Kauai, the geologically oldest of the Hawaiian Islands! You are getting closer to the Big Island of Hawaii. Let's play another round."),
        dict(place = 'Oahu',
            background = 'Sunset_next_to_Waikiki_Beach,_Oahu,_Hawai,_USA1.jpg',
            fluff = "Welcome to Oahu, the third-largest of the Hawaiian Islands! You are getting closer and closer to the Big Island. Let's play another round."),
        dict(place = 'Molokai',
            background = 'Church_at_the_end_of_the_road.jpg',
            fluff = "Welcome to Molokai, an island built from two shield volcanoes and one step closer to the Big Island. Let's play again."),
        dict(place = 'Lanai',
            background = 'Full_moon_setting_over_Lanai.jpg',
            fluff = "Welcome to Lanai, a comma-shaped island that was once covered with pineapple plantations. You're the nearest you've come to the Big Island yet, but which of you will make it there? Let's play another round."),
        dict(place = 'Maui',
            background = 'Kipahulu_coast.jpg',
            fluff = "Welcome to Maui, the second-largest of the Hawaiian Islands! You're almost there! Let's play again to see who will make it to the Big Island of Hawaii.")]
    
    round_wait = 2
    
    # The format of EEG trigger codes is as follows:
    #
    # Bits 0–2: Encodes the type of event.
    events = dict(
        # We skip 0 because that's a control code.
        subject_votes_to_accept   = 0b00000001,
        subject_votes_to_reject   = 0b00000010,
        subject_votes_neutral     = 0b00000011,
        subject_gets_accept_vote  = 0b00000100,
        subject_gets_reject_vote  = 0b00000101,
        subject_gets_neutral_vote = 0b00000110)
    # Bit 3: Encodes coplayer gender (0 male, 1 female).
    # Bits 4–6: Encodes the coplayer involved in the event. These
    #   ID numbers are gender-specific (e.g., male coplayer 3 and
    #   female coplayer 3 are different coplayers).
    # Bit 7: Always 0, avoiding confusion with codes 255 and 256
    #   (which are more control codes).
    def trigger_code(coplayer, event):
        return (
            (coplayer['trigger_id'] << 4) |
            (coplayer['female'] << 3) |
            events[event])
    
    button_box = {
      # Maps fingers to their fMRI button-box codes.
        'left pinkie':  '1',
        'left ring':    '2',
        'left middle':  '3',
        'left index':   '4',
        'left thumb':   '5',
        'right thumb':  '6',
        'right index':  '7',
        'right middle': '8',
        'right ring':   '9',
        'right pinkie': '0'}
    
    fmri_start_scanning_key = 'grave'
    
    # ------------------------------------------------------------
    # * Helper functions
    # ------------------------------------------------------------
    
    def shuffled(x): return sample(x, len(x))
    def choice(x): return shuffled(x)[0]
      # random.choice doesn't work on sets.
    
    def image_path(image):
        return par['image_dir'] + image
    
    big_canvas = Rect(o.win,
        width = 1.5, height = 1.8,
        fillColor = 'white', opacity = .8)
    strip_canvas = Rect(o.win,
        width = 1.2, height = .3,
        fillColor = 'white', opacity = .8)
    background_imagestim = ImageStim(o.win,
        image_path('Niihau_sep_2007.jpg'),
        units = 'pix',
        size = [o.screen_width, o.screen_height])
    
    def background(image_name):
        background_imagestim.setImage(image_path(image_name))
        return o.showing(background_imagestim, big_canvas)
    
    def message(duration, string):
        # Temporarily replace big_canvas with strip_canvas.
        with o.hiding(big_canvas):
            o.wait_screen(duration,
                strip_canvas,
                o.text(0, 0, string, wrap = 1.2))
    def fake_message(dkey, keys, string):
       # Look like `message`, but actually wait for a keypress instead
       # of waiting a fixed time.
        with o.hiding(big_canvas):
            o.keypress_screen(dkey, keys,
                strip_canvas,
                o.text(0, 0, string, wrap = 1.2))
    
    blank_background = o.hiding(background_imagestim, big_canvas)
    
    def lag(duration):
        message(duration, lag_msg)
    lag_msg = u'Waiting for all players to finish…'
    
    def write(write_point):
        # Don't use o.save in case we're inside a `dkey_prefix`.
        o.data['write_point'] = write_point
        p = par['output_path_fmt'].format(**o.data)
        o.write(p, json_default = json_default)
        print 'Data written to', p
    
    def json_default(x):
        if x is Reject:
            return -1
        elif x is Neutral:
            return 0
        elif x is Accept:
            return 1
        else:
            raise TypeError
    
    def simplify_gender(gender):
      # When the text string `gender` clearly identifies a binary gender,
      # return "Male" or "Female". Otherwise, just normalize capitalization.
        g = gender.lower()
        if g in ['m', 'male', 'b', 'boy', 'man']:
            return 'Male'
        if g in ['f', 'female', 'g', 'girl', 'w', 'woman']:
            return 'Female'
        return gender[0].upper() + gender[1:].lower()
    
    class TransformedRatingScale(RatingScale):
        def __init__(self, *args, **kwargs):
            self.transform = kwargs.pop('transform', None)
            RatingScale.__init__(self, *args, **kwargs)
    
        def getRating(self):
            v = RatingScale.getRating(self)
            if v is None or not self.transform:
                return v
            return self.transform(v)
    
    def rating_scale(y, num_options, **kwargs):
        rs = TransformedRatingScale(o.win, pos = (0, y),
            low = 1, high = num_options,
            textColor = 'black', lineColor = 'black',
            marker = 'circle', markerColor = 'black',
            stretch = 2,
            respKeys =
                [button_box[k] for k in (
                  'left pinkie', 'left ring', 'left middle',
                  'left index', 'left thumb', 'right thumb')[:num_options]]
                if par['fmri_mode']
                else [str(i) for i in range(1, num_options + 1)],
            acceptKeys = button_box['right index']
                if par['fmri_mode']
                else 'return',
            showValue = False, skipKeys = None, scale = None,
            showAccept = False,
            **kwargs)
        return rs
    
    def rating_scale_controls_text(num_options):
        fmri_choice_controls =  (
            {5: 'left hand', 6: 'left hand or right thumb'}[num_options])
        return o.text(0, -.7, wrap = 2, string =
            '{} - Choose an option\n{} - Confirm'.format(
                fmri_choice_controls if par['fmri_mode'] else 'number keys',
                'right index' if par['fmri_mode'] else 'Enter'))
    
    # ------------------------------------------------------------
    # * Coplayers
    # ------------------------------------------------------------
    
    class VoteType(object):
        def __init__(self, letter):
            self.letter = letter
        def __str__(self):
            return self.letter
    Reject = VoteType('R')
    Reject.key = button_box['left index'] if par['fmri_mode'] else 'f'
    Neutral = VoteType('N')
    Accept = VoteType('A')
    Accept.key = button_box['right index'] if par['fmri_mode'] else 'j'
    
    coplayers = dict(
    
        mean3 = dict(expendable = False,
            votes = (Reject, Reject, Reject, Neutral, Reject, Reject)),
        mean2 = dict(expendable = False,
            votes = (Reject, Reject, Neutral, Reject, Reject, Neutral)),
        mean1 = dict(expendable = False,
            votes = (Neutral, Reject, Reject, Accept, Reject, Neutral)),
        indiff = dict(expendable = False,
            votes = (Neutral, Neutral, Neutral, Reject, Accept, Neutral)),
        nice1 = dict(expendable = False,
            votes = (Accept, Neutral, Accept, Accept, Neutral, Reject)),
        nice2 = dict(expendable = False,
            votes = (Accept, Accept, Accept, Neutral, Neutral, Accept)),
        nice3 = dict(expendable = False,
            votes = (Accept, Accept, Neutral, Accept, Accept, Accept)),
    
        xpendable_rna = dict(expendable = True,
            votes = (Reject, Neutral, Accept, Reject, Neutral, Accept)),
        xpendable_ran = dict(expendable = True,
            votes = (Reject, Accept, Neutral, Reject, Accept, Neutral)),
        xpendable_nra = dict(expendable = True,
            votes = (Neutral, Reject, Accept, Neutral, Reject, Accept)),
        xpendable_nar = dict(expendable = True,
            votes = (Neutral, Accept, Reject, Neutral, Accept, Reject)),
        xpendable_arn = dict(expendable = True,
            votes = (Accept, Reject, Neutral, Accept, Reject, Neutral)),
        xpendable_anr = dict(expendable = True,
            votes = (Accept, Neutral, Reject, Accept, Neutral, Reject)))
    for k, p in sorted(coplayers.items()):
        p['id'] = k
        p['poll_responses'] = len(p['votes']) * [None]
    coplayers = coplayers.values()
    
    # Enable this block to show the properties of the matrix of votes
    # among the non-expendable coplayers.
    if False:
        mat = [cp['votes']
            for x in ('mean3', 'mean2', 'mean1', 'indiff', 'nice1', 'nice2', 'nice3')
            for cp in coplayers
            if cp['id'] == x]
        print 'Totals'
        for votetype in Reject, Neutral, Accept:
            print votetype, sum(1 for row in mat for v in row if v is votetype)
        print ''
        print 'Columns'
        ncol = len(mat[0])
        for votetype in Reject, Neutral, Accept:
            print votetype, ' '.join(
                str(sum(1 for row in mat if row[i] == votetype))
                for i in range(ncol))
        print ''
        print 'Rows'
        from collections import Counter
        for row in mat:
            d = Counter(row)
            print 'R {}, N {}, A {}'.format(d[Reject], d[Neutral], d[Accept])
        exit()
    
    # Decide what order the expendables will be kicked out. We choose
    # a random order that will result in the subject getting an equal
    # number of each type of vote.
    while True:
        kickout_order = shuffled([p for p in coplayers if p['expendable']])
        counts = Counter([vote
            for i, cp in enumerate(kickout_order)
            for vote in cp['votes'][: i + 1]])
        if len(counts.keys()) == len('RNA') and len(set(counts.values())) == 1:
            break
    o.save('coplayer_kickout_order', [p['id'] for p in kickout_order])
    
    # Make the coplayers evenly split by gender within the expendable
    # and non-expendable groups.
    for i, p in enumerate(shuffled([p for p in coplayers if p['expendable']])):
        p['female'] = bool(i % 2)
    for i, p in enumerate(shuffled([p for p in coplayers if not p['expendable']])):
        p['female'] = bool(i % 2)
      # Because there's an odd number of non-expendable coplayers,
      # we're left with one more male than we have females. Later,
      # if we learn that the subject is male, we'll make one of
      # the male non-expendables female.
    
    def pronoun_nom(p): return 'she' if p['female'] else 'he'
    def pronoun_obj(p): return 'her' if p['female'] else 'him'
    def pronoun_gen(p): return 'her' if p['female'] else 'his'
    
    # Assign names and portraits.
    us_males = zip(shuffled(us_male_names), shuffled(us_male_portraits),shuffled(hometown_us_male))
    inter_males = zip(shuffled(inter_male_names), shuffled(inter_male_portraits), shuffled(hometown_int_male))
    us_females = zip(shuffled(us_female_names), shuffled(us_female_portraits),shuffled(hometown_us_female))
    inter_females  = zip(shuffled(inter_female_names), shuffled(inter_female_portraits),shuffled(hometown_int_female))
    females = us_females + inter_females
    males = us_males + inter_males
    for p in coplayers:
        p['name'], p['portrait'],p['hometown']= females.pop() if p['female'] else males.pop()
    
    portrait_stim_cache = {}
    def portrait_stim(x, y, p, border_color = 'black'):
        img = par['subject_portrait_path'] if p is None else image_path(p['portrait'])
        k = x, y, border_color, img
        if k not in portrait_stim_cache:
            portrait_stim_cache[k] = StimGroup((
                ImageStim(o.win, pos = (x, y),
                    image = img),
                Rect(o.win, pos = (x, y),
                    width = (portrait_dims[0] + 3) / (.5 * o.screen_width),
                    height = (portrait_dims[1] + 3) / (.5 * o.screen_height),
                    lineColor = border_color, lineWidth = 3)))
        return portrait_stim_cache[k]
    
    # Assign fluff.
    for p, age, school, interest in zip(
            coplayers, shuffled(ages), shuffled(schools), shuffled(interests)):
        p['fluff'] = dict(
            Age = age, School = school, Interests = interest)
    o.save('coplayers', {p['id']: p for p in coplayers})
      # We don't copy the coplayer-objects because we want later edits
      # (such as the addition of poll responses) to be recorded.
    
    # ------------------------------------------------------------
    # * The likability-rating subroutine
    # ------------------------------------------------------------
    
    def rate_likabilities(time):
        num_options = 5
        cps = shuffled(o.data['coplayers'].values())
          # We don't just say `shuffled(coplayers)` because we want
          # the subject to rate coplayers that have been kicked out.
        o.save(('likability_rating', time, 'rating_order'),
            [p['id'] for p in cps])
        for p in cps:
            o.scale_screen(('likability_rating', time, 'ratings', p['id']),
                portrait_stim(-.5, .5, p),
                o.text(0, 0, 'How much do you like {}?'.format(p['name'])),
                rating_scale(y = -.2,
                    num_options = num_options,
                    labels = ['Not at all', 'Somewhat', 'Extremely']),
                rating_scale_controls_text(num_options = num_options))
    def rate_imposter(time):
        num_options = 5
        cps = shuffled(o.data['coplayers'].values())
          # We don't just say `shuffled(coplayers)` because we want
          # the subject to rate coplayers that have been kicked out.
        o.save(('imposter_rating', time, 'rating_order'),
            [p['id'] for p in cps])
        for p in cps:
            o.scale_screen(('imposter_rating', time, 'ratings', p['id']),
                portrait_stim(-.5, .5, p),
                o.text(0, 0, 'How much do you think {} will vote to keep you in the game?'.format(p['name'])),
                rating_scale(y = -.3,
                    num_options = num_options,
                    labels = ['Not at all', 'Somewhat', 'Extremely']),
                    rating_scale_controls_text(num_options = num_options))

    # ------------------------------------------------------------
    # * The voting subroutine
    # ------------------------------------------------------------
    
    icon_dim = 200 # Pixels
    icon_thickness = 10 # Pixels
    
    def icon_frame(x, color):
        kw = dict(units = 'pix', fillColor = color, lineColor = color)
        return [
            Rect(o.win, icon_dim, icon_thickness,
                pos = (x, icon_dim/2 - icon_thickness/2), **kw),
            Rect(o.win, icon_dim, icon_thickness,
                pos = (x, -icon_dim/2 + icon_thickness/2), **kw),
            Rect(o.win, icon_thickness, icon_dim,
                pos = (x + icon_dim/2, 0), **kw),
            Rect(o.win, icon_thickness, icon_dim,
                pos = (x - icon_dim/2, 0), **kw)]
    
    def reject_icon(x = 0, y = 0):
        return ImageStim(o.win, pos = (x, y),
            image = image_path('thumbs-down.png'))
    Reject.icon_c = reject_icon()
    
    def accept_icon(x = 0, y = 0):
        return ImageStim(o.win, pos = (x, y),
            image = image_path('thumbs-up.png'))
    Accept.icon_c = accept_icon()
    
    def neutral_icon(x = 0, y = 0):
        return Rect(o.win, width = .25, height = .5, pos = (x, y),
            fillColor = 'yellow',
            lineColor = 'gray', lineWidth = 10)
    Neutral.icon_c = neutral_icon()
    
    voting_time_limit = 5  # In seconds
    mean_postfeedback_wait = 4 if par['fmri_mode'] else 1.5  # In seconds
    
    def voting(nround):
    
        practice = nround is None
        if practice:
            cps = [
                dict(id = 'practice_a',
                     name = 'Player A', female = False,
                     portrait = 'example-male.png',
                     vote = Accept),
                dict(id = 'practice_b',
                     name = 'Player B', female = True,
                     portrait = 'example-female.png',
                     vote = Reject)]
        else:
            cps = shuffled(coplayers)
            o.save('vote_order', [p['id'] for p in cps])
    
        if par['fmri_mode']:
            # Create a randomly ordered set of post-feedback waits with
            # mean equal to `mean_postfeedback_wait`.
            postfeedback_waits = [mean_postfeedback_wait + x
                for i in range(1, len(cps) // 2 + 1)
                for x in (-.25 * i, .25 * i)]
            if len(cps) % 2:
                postfeedback_waits.append(mean_postfeedback_wait)
            postfeedback_waits = shuffled(postfeedback_waits)
            o.save('postfeedback_waits', postfeedback_waits)
        else:
            # Make every post-feedback wait equal to the mean.
            postfeedback_waits = [mean_postfeedback_wait] * len(cps)
    
        if par['fmri_mode'] and not practice:
            fake_message('begin_fmri',
                fmri_start_scanning_key,
                lag_msg)
    
        with blank_background:
    
            if par['fmri_mode']:
                o.wait_screen(5,
                    o.text(0, 0, color = 'white', string = "Use the buttons under your index fingers to vote. Voting will begin in a few seconds."))
            else:
                o.keypress_screen('start',
                    {Accept.key: 'Keep', Reject.key: 'Kick\nOut'},
                    o.text(0, 0, color = 'white', string = "Position your index fingers over the \"{Reject.key}\" and \"{Accept.key}\" keys. Then, press either one to begin voting.".format(**globals())))
    
            for i, p in enumerate(cps):
    
                # The subject votes.
                stimuli = [
                    portrait_stim(-.5, .5, p, border_color = 'white'),
                    o.html(.2, .8, vAlign = 'top', color = 'white', font_size = 14, string =
                        # Show the coplayer's profile.
                        '<b>{}</b><br><br>'.format(p['name']) +
                        '<b>{}</b><br>'.format('Female' if p['female'] else 'Male') +
                        ('' if practice else'<br>'.join(
                            ['<b>{}:</b> {}'.format(k, escape(p['fluff'][k])) for k in
                                ['Age', 'School', 'Interests']])))]
                voting_timer = CountdownTimer(voting_time_limit)
                o.keypress_screen(('subject_votes', p['id']),
                    {
                       voting_timer: TriggerKey('Neutral', None if practice else
                           trigger_code(p, 'subject_votes_neutral')),
                       Reject.key: TriggerKey('Kick\nOut', None if practice else
                           trigger_code(p, 'subject_votes_to_reject')),
                       Accept.key: TriggerKey('Keep', None if practice else
                           trigger_code(p, 'subject_votes_to_accept'))},
                    o.text(0, -.5, color = 'white', wrap = 2, string =
                        'Vote on ' + p['name']),
                    o.text(-.25, -.7, color = 'white', string =
                        '{} - Kick Out'.format(
                            'left' if par['fmri_mode'] else Reject.key)),
                    o.text(.25, -.7, color = 'white', string =
                        '{} - Keep'.format(
                            'right' if par['fmri_mode'] else Accept.key)),
                    *stimuli)
                o.wait_screen_till(voting_timer,
                    o.text(0, -.5, color = 'white', wrap = 2, string =
                        'Vote registered'),
                    *stimuli)
    
                # Show a fixation cross.
                o.wait_screen(2, o.fixation_cross)
    
                # Now show the coplayer's vote.
                pv = p['vote'] if practice else p['votes'][nround]
                if not practice: o.trigger(trigger_code(p, {
                    Reject: 'subject_gets_reject_vote',
                    Neutral: 'subject_gets_neutral_vote',
                    Accept: 'subject_gets_accept_vote'}[pv]))
                o.wait_screen(2, pv.icon_c)
    
                # Show a fixation cross again.
                o.wait_screen(postfeedback_waits[i], o.fixation_cross)
    
        if not practice:
          # An expendable coplayer is ousted.
            loser = kickout_order[nround]
            coplayers.remove(loser)
            o.wait_screen(5,
                portrait_stim(0, .5, loser),
                o.text(0, -.2, "And it's final decision time. Looks like {} got the most votes to go home! {} journey ends here. You get to continue on to the next island!".format(
                    loser['name'],
                    pronoun_gen(loser).capitalize())))
    
    # ------------------------------------------------------------
    # * Preliminaries
    # ------------------------------------------------------------
    
    o.save('mode', 'fmri' if par['fmri_mode'] else 'eeg')
    par['subject_portrait_path'] = 'subject-{}.jpg'.format(o.data['mode'])
    
    if par['debug']:
        o.data['subject'] = 'test'
    else:
        o.get_subject_id('Island Getaway - ' + o.data['mode'])
    
    subject_name = '???'
    
    o.start_clock()
    
    # ------------------------------------------------------------
    # * Introduction
    # ------------------------------------------------------------
    
    with background('Hawaje-NoRedLine.jpg'):
        message(2, 'Aloha!')
    
        with o.dkey_prefix('introduction'):
    
            o.instructions('set_the_scene', "Let's pretend you've just landed on the Hawaiian Island of Niihau to begin a summer vacation with a group of {} other college students. But the journey isn't over yet! First, you must make your way along the islands to get to the Big Island of Hawaii. Once there, your vacation will begin!".format(
                len(coplayers)))
    
            o.instructions('game_overview', "As you travel along the islands, you'll get to know more and more about the other players. After each round, you'll vote for who you would like to continue on to the Big Island with you and who you would like to send home. But the other players will also be voting on you! And your goal is to stay in the game and be one of the {} players (out of the original {}) who make it to the Big Island!".format(
                len(coplayers) + 1 - (len(round_descriptions) + 1),
                len(coplayers) + 1))
    
        with o.dkey_prefix('profile'):
    
            o.text_entry_screen('gender', 'Write in female?')
            o.data['profile']['gender'] = simplify_gender(o.data['profile']['gender'])
            if o.data['profile']['gender'] == 'Male':
                # Make a male non-expendable female so that there's
                # of equal number of male and female players.
                transgal = choice([p for p in coplayers if not p['female']])
                transgal['female'] = True
                transgal['name'] = choice(female_names - {p['name'] for p in coplayers if p['female']})
                transgal['portrait'] = choice(female_portraits - {p['portrait'] for p in coplayers if p['female']})
    
            o.text_entry_screen('name', 'What is your first name?')
            subject_name = o.data['profile']['name']
            # Try to normalize capitalization.
            if subject_name.isalpha() and (
                    subject_name.islower() or
                        (len(subject_name) > 2 and subject_name.isupper())):
                          # Don't downcase "AJ".
                subject_name = subject_name.lower().capitalize()
            # If the subject's name exactly matches the name of a
            # coplayer (case-insensitively), rename the coplayer.
            try:
                p = next(p for p in coplayers if
                    p['name'].lower() == subject_name.lower())
                p['name'] = extra_female_name if p['female'] else extra_male_name
            except StopIteration:
                pass
    
            o.nonneg_int_entry_screen('age', 'How old are you?')
            
            o.text_entry_screen('hometown', 'What is your hometown?')
    
            o.text_entry_screen('school', 'What school do you go to?')
    
            o.text_entry_screen('interests', "What are some things you're interested in?")
    
            o.okay_screen('view',
                portrait_stim(0, .5, None),
                o.html(0, 0,
                    subject_name + "<br><br>" +
                    '<b>{}</b><br>'.format(o.data['profile']['gender']) +
                    '<br>'.join(
                        '<b>{}:</b> {}'.format(k.capitalize(), escape(o.data['profile'][k])) for k in
                            ['age', 'school', 'interests','hometown'])))
    
        # Don't keep the profile data due to IRB shenanigans (for
        # the Kujawa lab at Penn State).
        del o.data['profile']
    
        lag(3)
    
    # Now that the coplayers' genders are set, we can assign trigger
    # codes.
    seen_genders = [0, 0]
    for p in coplayers:
        p['trigger_id'] = seen_genders[p['female']]
        seen_genders[p['female']] += 1
    
    write('intro')
    
    # ------------------------------------------------------------
    # * Round 0
    # ------------------------------------------------------------
    
    with o.dkey_prefix(('round', 0)), background('Niihau_sep_2007.jpg'):
    
        message(round_wait, 'Round 1: Niihau')
    
        o.instructions('read_profiles', 'Take a moment to learn about the other players.')
    
        cps = shuffled(coplayers)
        o.save('profile_order', [p['id'] for p in cps])
        for i, p in enumerate(cps):
            o.okay_screen(('fluff', i),
                portrait_stim(0, .5, p),
                o.html(0, 0,
                    '<b>{}</b><br>'.format(p['name']) +
                    '<b>{}</b><br>'.format('Female' if p['female'] else 'Male') +
                    '<b>{}</b>{}<br>'.format('Hometown: ',p['hometown']) +
                    '<br>'.join(
                        '<b>{}:</b> {}'.format(k, escape(p['fluff'][k])) for k in
                            ['Age', 'School', 'Interests'])))
    
        if par['fmri_mode']:
            ready_key = 'r'
            o.keypress_screen('fmri_setup',
                ready_key,
                o.text(0, 0, string = 'You may now enter the fMRI scanner.\n\nExperimenter, press the "{}" key when ready.'.format(ready_key)))
    
        rate_likabilities('pre')
        
        o.instructions('imposter', 'Please indicate how much you think others will vote to keep you in the game.')
        
        rate_imposter('pre')
    
        o.instructions('voting_begins', html = True, string = "And on to the first round of voting. Who do you want to send home? And who do you want to continue with on to the next island? You will now vote to kick out or keep each player. You have {voting_time_limit} seconds to vote. The player with the greatest percentage of votes to be sent home will be kicked off the island, with ties broken randomly.<br><br>Each time you vote, you will then find out how that player voted for you.".format(**globals()))
    
        o.okay_screen('feedback_explanation',
            o.text(0, .7, "For each player, after you've made your own vote, you'll see an icon that shows their vote."),
            accept_icon(-.5, .1),
            o.text(-.5, -.2, "This means a vote to keep you.",
                vAlign = 'top', wrap = .5),
            neutral_icon(0, .1),
            o.text(0, -.2, "This means no vote (possibly due to a network error).",
                vAlign = 'top', wrap = .5),
            reject_icon(.5, .1),
            o.text(.5, -.2, "This means a vote to kick you out.",
                vAlign = 'top', wrap = .5))
    
        with o.dkey_prefix('voting_practice'):
            o.instructions('intro', "First, you'll see two examples of how voting works.")
            voting(None)
            o.instructions('done', 'Now for the first round of real voting.')
    
        voting(0)
        write('voting-round-0')
    
    # ------------------------------------------------------------
    # * All other rounds
    # ------------------------------------------------------------
    
    for i, (r, (poll_question, poll_responses)) in enumerate(zip(round_descriptions, polls)):
        nround = i + 1
        with o.dkey_prefix(('round', nround)), background(r['background']):
    
            message(round_wait, 'Round {}: {}'.format(nround + 1, r['place']))
            o.instructions('fluff', r['fluff'])
    
            o.text_entry_screen('poll_question',
                "Now you'll all answer another question so you can get to know each other better.\n\n" +
                poll_question)
    
            for p, resp in zip(coplayers, shuffled(poll_responses)):
                p['poll_responses'][nround] = resp
            varwait = max(expovariate(2) for _ in coplayers)
            o.save('poll_varwait', varwait)
            lag(varwait)
    
            responses = shuffled(
                [(p['id'], p['name'], p['poll_responses'][nround]) for p in coplayers] +
                [('SUBJECT', subject_name, o.data['round'][nround]['poll_question'])])
            o.save('poll_response_order', [r[0] for r in responses])
            o.okay_screen('poll_results',
                o.text(0, .8, "Here are your responses:"),
                o.text(0, .65,
                    "\n".join(["{}: {}".format(r[1], r[2]) for r in responses]),
                    height = .06,
                    wrap = 1.4, vAlign = 'top'))
    
            voting(nround)
            write('voting-round-' + str(nround))
    
    # ------------------------------------------------------------
    # * A winner is you!
    # ------------------------------------------------------------
    
    with background('Rainbow_over_palms_at_Big_Island_of_Hawaii.jpg'):
        message(3, 'You made it to the Big Island of Hawaii!\nLet the vacation begin!')
    
        rate_likabilities('post')
    
    # ------------------------------------------------------------
    # * Post-game questionnaire
    # ------------------------------------------------------------
    
    refuse = 'I prefer not\nto answer'
    scale_levels = ('Not at all', 'Slightly', 'Somewhat', 'Quite a lot', 'Extremely', refuse)
    na_scale_level = scale_levels.index(refuse) + 1
    
    questions = [
        {'id': ('imposter question 1', 1), 'text': 'I have succeeded on in this game even though I was afraid that I would not do well.'},
        {'id': ('imposter question 2', 5), 'text': 'I feel or believe that my success in the game was the result of some kind of error.'},
        {'id': ('imposter question 3', 5), 'text': 'I feel my success in this game was due to some kind of luck.'},
        {'id': ('imposter question 4', 2), 'text': 'I remember the times other players voted to kick me out more than the times they voted to keep me in the game.'},
        {'id': ('imposter question 5', 3), 'text': 'I compared my ability to other players and thought they may be more intelligent than I am.'}]
    
    with o.dkey_prefix('postgame_questionnaire'), background('Rainbow_over_palms_at_Big_Island_of_Hawaii.jpg'):
        for q in questions:
            o.scale_screen(q['id'],
                o.text(0, .5, 'In this questionnaire, pick the options that best represent the feelings you were experiencing during the game.'),
                o.text(0, 0, q['text']),
                rating_scale(y = -.3,
                    num_options = len(scale_levels),
                    choices = scale_levels,
                    textSize = .8,
                    transform = lambda v:
                        'NA' if v == refuse else scale_levels.index(v) + 1),
                rating_scale_controls_text(num_options = len(scale_levels)))
    
    # ------------------------------------------------------------
    # * Done!
    # ------------------------------------------------------------
    
    o.done()
    write('done')
    
    o.wait_screen(1,
        o.text(0, 0, color = 'white', string = 'Done!\n\nPlease let the experimenter know you are done.'))
    
  finally:
    try:
        o.trigger_worker.terminate()
    except:
        pass
