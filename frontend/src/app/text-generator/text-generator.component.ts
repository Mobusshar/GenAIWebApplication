import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-text-generator',
  templateUrl: './text-generator.component.html',
  styleUrls: ['./text-generator.component.css']
})
export class TextGeneratorComponent implements OnInit {
  id: number = 0;
  prompt: string = '';
  response: string = `Ethan was indeed a very hardworking man who put in all his efforts in all possible ways. Every morning he woke up early and got prepared for work meticulously to support his family most effectively. But unfortunately, things started going totally non-synchronized, one fine day.

This particular morning, the alarm failed to ring, and therefore Ethan woke up late. In haste, he got up and started living his daily life. He wore a shirt on which some coffee spilled, and he got out just missing the usual bus. The rest of it was forced to be walked under a chilly and drizzling rain to get to work. Ethan noted how the rain fell and continued to match his steadily growing exasperation and sense of unluckiness. His shoes soaked through, his socks clung uncomfortably to his feet, and with each splash of a car passing by, he felt as though the universe was deliberately testing his patience.

Thanks to the plethora of obstacles piling up in his life, he had exceeded that last point and went further. He had finally made it to work, only to continue discovering frustration. His computer failed him on an important assignment, and everyone else seemed too busy burning their bridges to offer assistance. Every tiny mishap continued accumulating, leaving him tired and muffling up the morale. Ethan heaved a frustrated sigh, staring at his screen, feeling utterly defeated by everything around him. His fingers hovered over the keyboard, but no motivation remained. It felt like all his hard work, all his dedication, was for nothing. His mind screamed for a break, but there was no escape from the relentless cycle of bad luck.

Things couldn't get any worse—just as he thought. His boss called him into the office.

“Ethan, your work has been sloppy lately," said the boss coldly. He added, "If this continues, we may need to reconsider your position here." A sudden wave of fear gripped him. His breath hitched as a knot tightened in his stomach. His mind raced with the worst possibilities—what if he lost his job? What if he failed his family? The walls of the office suddenly seemed to close in on him, and the weight of his responsibilities pressed down on his chest, making it hard to breathe.

He had worked tireless days; now, one bad day could cost him everything. His hands trembled as he left the office; his heart was pounding.

At lunch hour, Ethan sat there alone, gripping a sandwich with white-knuckle fingers. One coworker bumped into him; his food hit the floor. "Hey, watch it, Ethan," the man dismissively muttered. That was the last straw. Anger erupted in Ethan's chest. His jaw clenched, and heat flared through his veins like wildfire. His fists tightened, and for a moment, he wanted to lash out—to yell, to push back. But as he stood abruptly, the shocked expressions of those around him made him swallow his rage. His heart pounded in his ears as he stormed out, his breaths coming in short, frustrated gasps.

After a rough day at work, in busy streets, Ethan walked home. Thousands of thoughts raced through his mind—frustration, worry, exhaustion, and everything in between. It was then that he saw an elderly lady standing at a very crowded sidewalk. Cars rushed past, and she looked like she didn't have the courage to cross such a busy road. Although he was so much into his own troubles, somehow there was that tug he could feel within him to help. He hesitated, torn between his own misery and the simple act of kindness. Then, without thinking further, he stepped forward.

He did stop for a moment. "I am already having my worst day. Why even bother?" But this egoistic thought was removed from his mind. Something very deep was urging him forward. He went to her and said, "May I help you cross the street?"

The eyes of the woman brightened up instantaneously with an illumination associated with relief. Tears welled up in her aged eyes, as if the smallest act of kindness had lifted a heavy burden off her shoulders.

"Oh, it would be a wonderful favor." He carefully took her across the street, shielding her from the impatience of rushing cars. He walked steadily beside her, making sure she felt safe. He noticed the frailty in her hands, the way she clung to his arm, trusting him completely in a world that often ignored people like her.

When they reached the other side of the street, the woman squeezed his hand, saying, "You have a very kind heart, young man."

At that moment, for the first time in a long time, something inside Ethan changed. A strange sense of peace settled within him, quieting the chaos of the day. It wasn’t much, but knowing he had made someone else's burden lighter brought a comfort he hadn’t felt in a long time.

Later that night, Ethan reached home only to find an unexpected surprise lying on his doorstep: a tiny little package along with a handwritten note. The note, written by the elderly lady, acknowledged her heartfelt gratitude. Within that package was a pair of gloves with a simple message inscribed, "Kindness is a reward."

Ethan's eyes went wide as he read the note, and warmth began to swell in his chest. A lump formed in his throat, not out of sadness, but out of something rare—joy. For the first time that day, he smiled, not out of habit, but genuinely.

It had changed the entire scenario; most importantly, it brought some happiness and brightness. Even on a day that felt like it was filled with constant misfortunes, it felt great to have one's kindness appreciated and recognized. In the end, it just goes to show that even on the worst days, a small act of kindness can change everything.

Inspired by the experience, he determined to keep helping others, no matter how difficult his own circumstances became.

The next morning came into play with the strangest of happenings. As he entered his work, he saw the coworker whom he had snapped at yesterday. It would have been easy to ignore him, but instead, Ethan took a breath and said, "Hey... I'm sorry about yesterday." The man blinked at him in surprise, then laughed and said, "No worries, Ethan. I was in a bad mood too." Then they shook hands, and for the first time ever, Ethan felt a sense of kinship with another human being in the workplace.

Thus, Ethan was called again by his boss, only this time the tone was entirely different. "I've been watching you, Ethan. I see improvement. Keep it up." Relief flooded Ethan's chest. He exhaled, feeling as if the weight of the world had been lifted off his shoulders.

He was convinced he might well have been on the verge of losing everything; instead, there turned out to be a way forward.

He could feel the care for others in him—from within. He now knew how much people's suffering mirrored his own, and for the first time, he felt other people's pain with a weight never felt before. He no longer saw others as obstacles to his own success but as people carrying invisible burdens of their own.

He sat in silent deliberation, understanding what this harsh day really meant for him. He had thought that suffering hardship meant only pain but had now discovered the hidden meaning within. It was not just about enduring—suffering had the power to transform.

As a bright candle of hope, his story spread all over the community. People started thinking that no matter how wrong life seems at times, small acts of generosity and care could create ripples of change. The unlucky day for Ethan became a historic day—proving that every challenge has a chance to make this world a bit brighter.`;

  story_character: string = '';
  
  frustration: string = '';
  sadness: string = '';
  fear: string = '';
  anger: string = '';
  empathy: string = '';
  gratitude: string = '';
  protectiveness: string = '';
  serenity: string = '';
  joy: string = '';
  hope: string = '';
  friendship: string = '';
  relief: string = '';
  compassion: string = '';
  self_reflection: string = '';
  inspiration: string = '';
  story_moral: string = '';
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log('Received ID:', this.id);
    this.fetchStoryData();
  }

  fetchStoryData() {
    this.http.get<any>(`${this.apiUrl}/exercise1/get-story/${this.id}`)
      .subscribe(
        data => {
          console.log("Fetched Story Data:", data);
          this.story_character = data.story_character;
          this.frustration = data.frustration;
          this.sadness = data.sadness;
          this.fear = data.fear;
          this.anger = data.anger;
          this.empathy = data.empathy;
          this.gratitude = data.gratitude;
          this.protectiveness = data.protectiveness;
          this.serenity = data.serenity;
          this.joy = data.joy;
          this.hope = data.hope;
          this.friendship = data.friendship;
          this.relief = data.relief;
          this.compassion = data.compassion;
          this.self_reflection = data.self_reflection;
          this.inspiration = data.inspiration;
          this.story_moral = data.story_moral;
        },
        error => {
          console.error("API Error:", error);
          alert(`Error: ${error?.error?.error || 'Something went wrong while fetching the story data'}`);
        }
      );
  }

  sendMessage() {
    if (!this.prompt.trim()) {
      alert("Please enter a prompt.");
      return;
    }

    console.log("Sending API request...");

    const requestPayload = {
      prompt: this.prompt 
    }; // Prepare the request payload with the additional fields

    // Send POST request to Flask backend
    this.http.post<{ response: string }>(`${this.apiUrl}/chat`, requestPayload)
      .subscribe(
        response => {
          console.log("API Response:", response); 
          this.response = response.response;
        },
        error => {
          console.error("API Error:", error); // Log any error response from the API
          alert(`Error: ${error?.error?.error || 'Something went wrong while generating the response'}`);
        }
      );
  }

  navigateBack() {
    this.router.navigate(['/story-building', this.id]);
  }
  
  navigateToSubmitExercise1() {
    this.router.navigate(['/submit-exercise1', this.id]);
  }
}
