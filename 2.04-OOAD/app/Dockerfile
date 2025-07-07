FROM ruby:3.4.4-alpine

WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN bundle config set without 'development' \
 && bundle install

COPY . .

CMD ["ruby", "app.rb"]
